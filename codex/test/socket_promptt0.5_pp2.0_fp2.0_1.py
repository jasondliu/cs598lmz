import socket
# Test socket.if_indextoname()
import sys
import time

from framework import VppTestCase, VppTestRunner
from vpp_ip import DpoProto
from vpp_ip_route import VppIpRoute, VppRoutePath, VppIpMRoute, \
    VppMRoutePath, VppIpTable, MRouteItfFlags, MRouteEntryFlags, \
    VppIpMRouteBind, MRouteBindFlags
from vpp_neighbor import VppNeighbor
from vpp_papi import VppEnum
from vpp_l2 import VppBridgeDomain, VppBridgeDomainPort

from scapy.packet import Raw
from scapy.layers.l2 import Ether, ARP, GRE
from scapy.layers.inet import IP, UDP, ICMP, TCP
from scapy.layers.inet6 import IPv6, ICMPv6TimeExceeded
from scapy.contrib.mpls import MPLS

from util import ppp

# TODO:
# 1. Add a test case to test when we have multiple paths to a destination
