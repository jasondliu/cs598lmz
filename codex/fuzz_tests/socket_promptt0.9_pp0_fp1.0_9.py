import socket
# Test socket.if_indextoname()
import unittest
from unittest import mock
import errno
import logging

from multiprocessing import Manager

from scapy.layers.inet import IP
from scapy.layers.inet6 import IPv6, ICMPv6ND_RouterSolicit
from scapy.layers.l2 import Ether
import scapy.compat
from scapy.config import conf
from scapy.supersocket import L3RawSocket
from scapy.utils import mac2str
from scapy.sendrecv import sniff
from scapy.arch import pcapdnet
from scapy.arch.windows import OperationsError
from scapy.utils6 import in6_islladdr
from scapy.arch.linux import SIOCGIFINDEX

from af_packet import *
from af_packet.constants import TPACKET_V2
from af_packet.socket import *
from af_packet.parser_macros import define_packet_parsing_macros
from af_packet.masks import *
from af_packet.tp_pack
