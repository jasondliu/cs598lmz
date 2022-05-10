import socket
import subprocess

from scapy.all import *
from scapy.layers.inet import *
from scapy.layers.dhcp import *
from scapy.layers import dhcp

class Responder(object):

	def __init__(self, timeout=1, verbose=False):
		if not verbose:
			sniff(prn=self.handle_packet, filter="udp", store=0, timeout=timeout)

	def handle_packet(self, packet):
		if DHCP in packet:
			self.handle_dhcp_packet(packet)
		else:
			pass

	def handle_dhcp_packet(self, packet):
		if packet[DHCP].options[0][1]==1:
			self.handle_dhcp_discover(packet)

	def handle_dhcp_discover(self, packet):
		print("DHCPDiscover")
		answer = packet
		answer[DHCP].options = []
		answer[BO
