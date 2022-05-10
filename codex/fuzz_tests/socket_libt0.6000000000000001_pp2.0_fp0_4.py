import socket
import sys
import time
import urllib

import bs4
import requests

class Proxy(object):
    def __init__(self, host, port, scheme, timeout):
        self.host = host
        self.port = port
        self.scheme = scheme
        self.timeout = timeout

    def __str__(self):
        return '{}://{}:{}'.format(self.scheme, self.host, self.port)

    def __repr__(self):
        return self.__str__()

class ProxyChecker(object):
    def __init__(self, proxy, timeout=10, url='http://www.google.com'):
        self.proxy = proxy
        self.timeout = timeout
        self.url = url

    def check(self):
        try:
            proxies = {
                'http': str(self.proxy),
                'https': str(self.proxy)
            }
            resp = requests.get(self.url, proxies=proxies, timeout=self.timeout)
            if resp.status
