import select
import socket
import sys
import threading
import time
import traceback

from dnslib import DNSHeader, DNSRecord, QTYPE, RR, dns

from . import config
from . import util
from . import logging
from . import dns_relay
from . import dns_cache

try:
    import asyncio
except ImportError:
    asyncio = None

try:
    import uvloop
except ImportError:
    uvloop = None

logger = logging.getLogger(__name__)


class TCPRelay(object):

    def __init__(self, config, dns_servers, is_local, stat_callback=None, cache=None):
        self._config = config
        self._dns_servers = dns_servers
        self._is_local = is_local
        self._cache = cache
        self._stat_callback = stat_callback
        self._dns_client = dns_relay.DNSClient(dns_servers, is_local, cache=cache)
        self
