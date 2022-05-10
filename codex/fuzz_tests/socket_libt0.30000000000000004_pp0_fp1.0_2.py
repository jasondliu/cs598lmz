import socket
import sys
import os
import time
import threading
import struct
import binascii
import random
import datetime

from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether
from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest
from scapy.layers.inet6 import IPv6ExtHdrFragment, IPv6ExtHdrRouting
from scapy.layers.inet6 import IPv6ExtHdrHopByHop, IPv6ExtHdrDestOpt
from scapy.layers.inet6 import IPv6ExtHdrFragment, IPv6ExtHdrRouting
from scapy.layers.inet6 import IPv6ExtHdrHopByHop, IPv6ExtHdrDestOpt
from scapy.layers.inet6 import IPv6ExtHdrFragment, IPv6ExtHdrRouting
from scapy.layers.inet6 import IPv6ExtHdrHopByHop, IPv6ExtHdrDestOpt
from scapy.layers.inet6
