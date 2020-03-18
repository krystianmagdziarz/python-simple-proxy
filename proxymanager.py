from proxysources.proxypub import ProxyPub
from proxysources.fateproxy import FateProxy
from abstract.services import ProxyServices


class ProxyManager(ProxyServices):
    __proxy_pub = None
    __fate_proxy = None

    @property
    def proxy_pub(self) -> ProxyPub:
        if ProxyManager.__proxy_pub is None:
            ProxyManager.__proxy_pub = ProxyPub()
            return ProxyManager.__proxy_pub
        else:
            return ProxyManager.__proxy_pub

    @proxy_pub.setter
    def proxy_pub(self, instance):
        self.__proxy_pub = instance

    @property
    def fate_proxy(self) -> FateProxy:
        if ProxyManager.__fate_proxy is None:
            ProxyManager.__fate_proxy = FateProxy()
            return ProxyManager.__fate_proxy
        else:
            return ProxyManager.__fate_proxy

    @fate_proxy.setter
    def fate_proxy(self, instance):
        self.__fate_proxy = instance

    def get_all(self):
        """
        Get all unique proxy from sources
        :return: List<Proxy>
        """
        attr = [
            self.proxy_pub,
            self.fate_proxy,
        ]

        for proxy_array in attr:
            for single_proxy in proxy_array.get_proxies_list():
                self.add_new_proxy(proxy=single_proxy)

        return self.get_proxies_list()

    def print_all(self):
        """
        Print all proxies to console
        :return: None
        """
        all_proxy = self.get_all()
        for proxy in all_proxy:
            print(proxy)

