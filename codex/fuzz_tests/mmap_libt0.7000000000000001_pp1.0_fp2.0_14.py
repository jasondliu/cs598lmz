import mmap
import os
import socket
import struct
import subprocess
import sys

# Try to import the Python 2 modules and fallback to Python 3 if necessary.
try:
    from ConfigParser import ConfigParser
    from Queue import Queue
except ImportError:
    from configparser import ConfigParser
    from queue import Queue

# Import our own modules.
from dnslib import A, AAAA, CNAME, DNSHeader, DNSLabel, DNSRecord, QTYPE
from dnslib.server import DNSServer, DNSHandler, BaseResolver

HOST_ADDRESS = '::'
HOST_PORT = 53

PID_FILE = '/var/run/powerdns.pid'

RESOLVER_CONF = '/etc/resolv.conf'

# We will only use the first nameserver.
NAMESERVER = None

# Used to cache DNS records.
RECORD_CACHE = dict()
RECORD_CACHE_SIZE = 100
RECORD_TTL = 60

# Used to cache resolved IP addresses.
IP_CACHE = dict
