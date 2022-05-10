import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 53))

# import ipaddress
# ipaddress.ip_interface('192.168.1.1/24')
# ipaddress.ip_address('192.168.1.1')
# ipaddress.ip_network('192.168.1.0/24')

# import struct

import sys
import time
# from dnslib import *

# import dns.message
# import dns.name
# import dns.query
# import dns.resolver
# import dns.reversename
# import dns.rdatatype
# import dns.rdataclass
# import dns.rdtypes.ANY.SOA
# import dns.rdtypes.ANY.A
# import dns.rdtypes.ANY.AAAA
# import dns.rdtypes.ANY.NS
# import dns.rdtypes.ANY.CNAME
# import dns.rdtypes.ANY.MX
# import dns
