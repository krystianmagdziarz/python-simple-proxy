import requests

from random import randint
from bs4 import BeautifulSoup


class ProxyServices:

    def __init__(self):
        self._proxy_array = []
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

    def add_new_proxy(self, ip: str, port: str, protocol="http", country="US", anonymity="low"):
        """
        Add new proxy to array
        :param ip: Proxy ip
        :param port: Proxy port
        :param protocol: Proxy protocol
        :type country: Proxy country
        :param anonymity: Anonymity level
        :return: None

        """
        self._proxy_array.append({
            "ip": ip,
            "port": port,
            "protocol": protocol,
            "country": country,
            "anonymity": anonymity,
            "used": 0,
            "errors": 0
        })

    def get_proxies_array(self):
        """
        Get proxies array
        :return: Array<Proxy>
        """
        return self._proxy_array

    def get_random(self):
        """
        Get random proxy
        :return: Proxy object
        """
        return None if len(self._proxy_array) == 0 else self._proxy_array[randint(0, len(self._proxy_array) - 1)]

    def get_next(self):
        """
        Get nex proxy from collection. Rotate mode.
        Ordering asc by used.
        :return:
        """
        return sorted(self._proxy_array, key=lambda k: k['used'])[0]

    def erase_proxy_array(self):
        """
        Erase all index from proxy array
        :return: Empty proxy array Array[]
        """
        del self._proxy_array[:]
        return self.get_proxies_array()

    def mark_proxy_error(self, proxy: str, port: str) -> bool:
        """
        Add error occurrence for specific proxy
        :param proxy: Proxy ip
        :param port: Proxy port
        :return: Status
        """
        for x in self._proxy_array:
            self.clear_bad_proxy(x)
            if x["ip"] is proxy and x["port"] is port:
                x["errors"] += 1
                return True
        return False

    def mark_proxy_used(self, proxy: str, port: str) -> bool:
        """
        Mark use of proxy
        :param proxy: Proxy ip
        :param port: Proxy port
        :return: Status
        """
        for x in self._proxy_array:
            if self.is_active_used_limit:
                self.clear_bad_proxy(x)
            if x["ip"] is proxy and x["port"] is port:
                x["used"] += 1
                return True
        return False

    def clear_bad_proxy(self, proxy):
        """
        Check if proxy is bad and remove if is
        :param proxy: Proxy object
        """
        if proxy["errors"] > self.error_limit:
            self._proxy_array.remove(proxy)

    def clear_used_proxy(self, proxy):
        """
        Check if proxy is used and remove if is
        :param proxy: Proxy object
        """
        if proxy["used"] > self.used_limit:
            self._proxy_array.remove(proxy)

    def clear_all_bad_proxies(self):
        """
        Remove all bad proxy from list
        :return: Array<Proxy>
        """
        for x in self._proxy_array:
            self.clear_bad_proxy(x)
        return self.get_proxies_array()

    def clear_all_used_proxies(self):
        """
        Remove all used proxy from list
        :return: Array<Proxy>
        """
        for x in self._proxy_array:
            self.clear_used_proxy(x)
        return self.get_proxies_array()

    def _get_url(self, proxy_url):
        r = requests.get(proxy_url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
        })

        return BeautifulSoup(r.text, "lxml")

    def __str__(self):
        return "\n".join(":".join((x["ip"], x["port"])) + " "
                         + "|".join((x["protocol"], x["country"], x["anonimity"], x["used"]))
                         for x in self._proxy_array)

    def __len__(self):
        return len(self._proxy_array)
