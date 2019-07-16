from .free_proxy import FreeProxy
from .proxy_pub import ProxyPub
from .fate_proxy import FateProxy


class ProxyManager:
    __free_proxy = None
    __proxy_pub = None
    __fate_proxy = None

    @staticmethod
    def get_free_proxy() -> FreeProxy:
        if ProxyManager.__free_proxy is None:
            ProxyManager.__free_proxy = FreeProxy()
            return ProxyManager.__free_proxy
        else:
            return ProxyManager.__free_proxy

    @staticmethod
    def get_proxy_pub() -> ProxyPub:
        if ProxyManager.__proxy_pub is None:
            ProxyManager.__proxy_pub = ProxyPub()
            return ProxyManager.__proxy_pub
        else:
            return ProxyManager.__proxy_pub

    @staticmethod
    def get_fate_proxy() -> FateProxy:
        if ProxyManager.__fate_proxy is None:
            ProxyManager.__fate_proxy = FateProxy()
            return ProxyManager.__fate_proxy
        else:
            return ProxyManager.__fate_proxy
