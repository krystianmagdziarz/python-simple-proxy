from proxymanager.proxysources.free_proxy import FreeProxy
from proxymanager.proxysources.proxy_pub import ProxyPub
from proxymanager.proxysources.fate_proxy import FateProxy


class ProxyManager:
    __free_proxy = None
    __proxy_pub = None
    __fate_proxy = None

    @property
    def free_proxy(self) -> FreeProxy:
        if ProxyManager.__free_proxy is None:
            ProxyManager.__free_proxy = FreeProxy()
            return ProxyManager.__free_proxy
        else:
            return ProxyManager.__free_proxy

    @free_proxy.setter
    def free_proxy(self, instance):
        self.__free_proxy = instance

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
