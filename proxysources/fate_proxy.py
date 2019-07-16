from proxymanager.abstract.proxy_services import ProxyServices

import json


class FateProxy(ProxyServices):
    FATE_PROXY_URL = "https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list"

    def __init__(self):
        """
        Get new proxy from source
        """
        super().__init__()
        self.get_new()

    def get_new(self, only_htts=False):
        bs = self._get_url(self.FATE_PROXY_URL)

        # Find github README.md box
        github_raw = bs.find("p").text

        for x in github_raw.splitlines():
            json_loads = json.loads(x)

            if only_htts:
                if json_loads["type"] is "https":
                    self.add_new_proxy(
                        json_loads["host"],
                        json_loads["port"],
                        json_loads["type"],
                        json_loads["country"],
                        json_loads["anonymity"]
                    )
            else:
                self.add_new_proxy(
                    json_loads["host"],
                    json_loads["port"],
                    json_loads["type"],
                    json_loads["country"],
                    json_loads["anonymity"]
                )

        return self.get_proxies_list()

