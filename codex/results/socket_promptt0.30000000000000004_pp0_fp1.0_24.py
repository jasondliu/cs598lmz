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


class SocketHook(object):
    def __init__(self, snaplen=SNAPLEN, promisc=False, immediate=False,
                 timeout=None, monitor=False, rfmon=False,
                 filter=None, nofilter=False,
                 to_ms=None, from_file=None, to_file=None,
                 to_pcap=None, to_pcapng=None, to_socket=None,
                 to_stdout=False, to_stderr=False, to_list=False,
                 to_callback=None, to_stop=None, to_stop_callback=None,
                 to_stop_count=None, to_stop_duration=None,
                 to_stop
