from proxymanager.abstract.proxy_services import ProxyServices


class FreeProxy(ProxyServices):
    FREE_PROXY_URL = "https://github.com/dxxzst/free-proxy-list"

    def __init__(self):
        """
        Get new proxy from source
        """
        super().__init__()
        self.get_new()

    def get_new(self, only_htts=False):
        bs = self._get_url(self.FREE_PROXY_URL)

        # Find github README.md box
        github_box_body = bs.find("div", {"class": "Box-body"})

        if github_box_body:
            # Get table ROWS
            tbody = github_box_body.find("tbody")
            tr = tbody.find_all("tr")

            for x in tr:
                td = x.find_all("td")
                ip = td[0].text
                port = td[1].text
                protocol = td[2].text
                anonymity = td[3].text
                country = td[4].text

                if not only_htts:
                    self.add_new_proxy(
                        ip=ip,
                        port=port,
                        protocol=protocol,
                        anonymity=anonymity,
                        country=country
                    )
                else:
                    if protocol == "https" or protocol == "https:":
                        self.add_new_proxy(
                            ip=ip,
                            port=port,
                            protocol=protocol,
                            anonymity=anonymity,
                            country=country
                        )

        return self.get_proxies_list()

