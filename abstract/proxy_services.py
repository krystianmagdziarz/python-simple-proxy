import requests

from random import randint
from bs4 import BeautifulSoup

from proxymanager.abstract.proxy import Proxy


class ProxyServices:

    def __init__(self):
        self._proxy_list = []
        self._used_limit = False
        self._proxy_limit_error = 5
        self._proxy_limit_used = 30

    @property
    def used_limit(self):
        return self._proxy_limit_used

    @used_limit.setter
    def used_limit(self, limit):
        self._proxy_limit_used = limit

    @property
    def error_limit(self):
        return self._proxy_limit_error

    @error_limit.setter
    def error_limit(self, limit):
        self._proxy_limit_error = limit

    @property
    def is_active_used_limit(self):
        return self._used_limit

    @is_active_used_limit.setter
    def is_active_used_limit(self, state):
        self._used_limit = state

    def add_new_proxy(self, **kwargs):
        """
        Add new proxy to array
        :param ip: Proxy ip
        :param port: Proxy port
        :param protocol: Proxy protocol
        :type country: Proxy country
        :param anonymity: Anonymity level
        :return: None

        """

        if(len(kwargs)) == 2:
            new_proxy = Proxy(kwargs["ip"], kwargs["port"])
        elif (len(kwargs)) == 5:
            new_proxy = Proxy(kwargs["ip"], kwargs["port"], kwargs["protocol"], kwargs["country"], kwargs["anonymity"])
        elif (len(kwargs)) == 1:
            if isinstance(kwargs["proxy"], Proxy):
                new_proxy = kwargs["proxy"]
            else:
                raise NotImplementedError
        else:
            raise NotImplementedError

        if new_proxy not in self._proxy_list:
            self._proxy_list.append(new_proxy)

    def get_proxies_list(self):
        """
        Get proxies array
        :return: List<Proxy>
        """
        return self._proxy_list

    def get_random(self):
        """
        Get random proxy
        :return: Proxy object
        """
        return None if len(self._proxy_list) == 0 else self._proxy_list[randint(0, len(self._proxy_list) - 1)]

    def get_next(self):
        """
        Get nex proxy from collection. Rotate mode.
        Ordering asc by used.
        :return:
        """
        return sorted(self._proxy_list, key=lambda k: k.used)[0]

    def erase_proxy_array(self):
        """
        Erase all index from proxy array
        :return: Empty proxy array Array[]
        """
        del self._proxy_list[:]
        return self.get_proxies_list()

    def mark_proxy_error(self, proxy: str, port: str) -> bool:
        """
        Add error occurrence for specific proxy
        :param proxy: Proxy ip
        :param port: Proxy port
        :return: Status
        """
        for x in self._proxy_list:
            self.clear_bad_proxy(x)
            if x.ip is proxy and x.port is port:
                x.errors += 1
                return True
        return False

    def mark_proxy_used(self, proxy: str, port: str) -> bool:
        """
        Mark use of proxy
        :param proxy: Proxy ip
        :param port: Proxy port
        :return: Status
        """
        for x in self._proxy_list:
            if self.is_active_used_limit:
                self.clear_bad_proxy(x)
            if x.ip is proxy and x.port is port:
                x.used += 1
                return True
        return False

    def clear_bad_proxy(self, proxy):
        """
        Check if proxy is bad and remove if is
        :param proxy: Proxy object
        """
        if proxy.errors > self.error_limit:
            self._proxy_list.remove(proxy)

    def clear_used_proxy(self, proxy):
        """
        Check if proxy is used and remove if is
        :param proxy: Proxy object
        """
        if proxy.used > self.used_limit:
            self._proxy_list.remove(proxy)

    def clear_all_bad_proxies(self):
        """
        Remove all bad proxy from list
        :return: List<Proxy>
        """
        for x in self._proxy_list:
            self.clear_bad_proxy(x)
        return self.get_proxies_list()

    def clear_all_used_proxies(self):
        """
        Remove all used proxy from list
        :return: List<Proxy>
        """
        for x in self._proxy_list:
            self.clear_used_proxy(x)
        return self.get_proxies_list()

    def _get_url(self, proxy_url):
        r = requests.get(proxy_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        })

        return BeautifulSoup(r.text, "lxml")

    def __str__(self):
        return "\n".join(":".join((x.ip, x.port)) + " "
                         + "|".join((x.protocol, x.country, x.anonymity, str(x.used), str(x.errors)))
                         for x in self._proxy_list)

    def __len__(self):
        return len(self._proxy_list)
