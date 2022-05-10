import select
import socket
import sys
import threading
import time
import traceback

import dns.message
import dns.name
import dns.query
import dns.rcode
import dns.rdataclass
import dns.rdatatype
import dns.resolver

from . import config
from . import logger
from . import util


class DNSProxy(object):
    def __init__(self, config):
        self.config = config
        self.logger = logger.Logger(config.log_level)
        self.dns_resolver = dns.resolver.Resolver()
        self.dns_resolver.nameservers = config.dns_server
        self.dns_resolver.timeout = config.dns_timeout
        self.dns_resolver.lifetime = config.dns_timeout
        self.dns_resolver.retry_servfail = True
        self.dns_resolver.rotate = True
        self.dns_resolver.cache = None
        self.dns_
