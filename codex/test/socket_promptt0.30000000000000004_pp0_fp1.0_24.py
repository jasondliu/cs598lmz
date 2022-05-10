import socket
# Test socket.if_indextoname()
import sys
import time

from . import util

from . import dpkt
from . import ip
from . import ip6
from . import tcp
from . import udp
from . import pcap

from . import pcapng

# XXX - should we use the same default as tcpdump?
SNAPLEN = 65535


