import socket
import threading

import dns.resolver
import dns.reversename

from core.logger import logger

log = logger()


class DnsLookup():
    def __init__(self):
        self.timeout = 2
        self.lock = threading.Lock()
        self.resolver = dns.resolver.Resolver()
        self.resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        self.resolver.timeout = self.timeout
        self.resolver.lifetime = self.timeout

    def lookup_ip(self, ip):
        try:
            rev_name = dns.reversename.from_address(ip)
            name = str(self.resolver.query(rev_name, "PTR")[0])
            return name
        except Exception as e:
            log.debug(e)
            return None

    def lookup_name(self, name):
        try:
            answer = self.resolver.query(name)
            return str(answer
