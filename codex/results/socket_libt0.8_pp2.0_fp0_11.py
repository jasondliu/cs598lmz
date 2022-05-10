import socket
import subprocess
import time

from scapy.all import *

class Net_scanner():
	"""docstring for Net_scanner"""
	def __init__(self):
		pass

	def get_target_network(self):
		output = subprocess.check_output(['ifconfig'])
		interface = re.search(r'en0',output).group(0)
		network = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',output.split('en0')[1]).group(0)
		split_network = network.split('.')
		split_network = split_network[:3]
		split_network = '.'.join(split_network)
		return interface,split_network

	def get_target_IP(self):
		target_network,interface = self.get_target_network()
		output = subprocess.check_output(['sudo','nmap','-sP',
