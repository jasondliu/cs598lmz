import socket
socket.if_indextoname("7")

import dpkt
import pcap
import os
import sys
import socket
import ipaddress
import datetime
import binascii
from scapy.all import *
from datetime import datetime
from datetime import timedelta
from dpkt.compat import compat_ord
from dpkt.compat import compat_struct_pack
from dpkt.compat import compat_struct_unpack
from dpkt.compat import compat_struct_calcsize
from dpkt.compat import compat_inet_ntop
from dpkt.compat import compat_inet_pton


def mac_addr(address):
	"""Convert a MAC address to a readable/printable string

	Args:
		address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
	Returns:
		str: Printable/readable MAC address
	"""
	return ':'.join('%02x' % compat_ord(b) for b in address)


def in
