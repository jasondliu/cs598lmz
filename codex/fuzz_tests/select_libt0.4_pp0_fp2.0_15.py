import select
import socket
import sys
import time
import traceback
from types import *

import pcap

from . import dns
from . import dpkt
from . import ethernet
from . import ip
from . import ip6
from . import loopback
from . import loopback6
from . import ppp
from . import raw
from . import sll
from . import tcp
from . import udp
from . import utils
from . import vlan

# XXX - use bytes for python3

# pcap dumper
class Dumper(object):
    def __init__(self, *args):
        self.__dumper = pcap.pcapObject.dump_open(*args)

    def __del__(self):
        self.__dumper.dump_close()

    def __getattr__(self, name):
        return getattr(self.__dumper, name)

# pcap reader
class Reader(object):
    def __init__(self, *args):
        self.__reader = pcap.pcapObject.open_live(*args)
