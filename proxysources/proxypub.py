from abstract.services import ProxyServices


class ProxyPub(ProxyServices):
    PROXY_PUB_URL = "http://pubproxy.com/api/proxy?limit=5&format=txt&https=true&type=https"

    def __init__(self):
        """
        Get new proxy from source
        """
        super().__init__()
        self.get_new()

    def get_new(self, only_htts=False):
        bs = self._get_url(self.PROXY_PUB_URL)

        proxy_lines = bs.find("p").text

        for x in proxy_lines.splitlines():
            if x is not None:
                single_proxy = x.split(":")
                self.add_new_proxy(
                    ip=single_proxy[0],
                    port=single_proxy[1],
                    protocol="https",
                    country="",
                    anonymity="")

        return self.get_proxies_list()
