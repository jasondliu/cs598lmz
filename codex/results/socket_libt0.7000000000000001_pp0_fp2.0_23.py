import socket
import struct
from datetime import datetime

from ipwhois import IPWhois
from pymongo import MongoClient
from tld import get_tld
from docopt import docopt

from domain_without_dots import Domain
from timer import Timer


class IPData:
    def __init__(self, ip_address, ip_version):
        self.ip_address = ip_address
        self.ip_version = ip_version
        self.port = 0
        self.ip_whois = None
        self.domain = None
        self.tld = None
        self.domain_len = None
        self.domain_without_dots = None
        self.domain_without_dots_len = None
        self.domain_without_dots_len_div_domain_len = None
        self.ns_count = None
        self.ns_len_avg = None
        self.asn = None
        self.asn_cidr = None
        self.is_dynamic = None
        self.country = None
        self
