import ctypes
import ctypes.util
import threading
import sqlite3
import tempfile
import os
import sys
import contextlib
import base64
import textwrap
import ipaddr

from client import is_server
from client import trace
from common.gedditdb import create_database, get_connection
from common.utils import get_mount_points
from common.tcpdump import start_tcpdump, stop_tcpdump

class VBox(object):

	@staticmethod
	def create_hostonly_if(name, ip_address, netmask):
		#create a new host only interface for the vm
		machine = ClientLib.get_virtualbox().createMachine('', name, [], '', '')
		#network= ClientLib.get_virtualbox().createDHCPServer('Host-only Network')
		network = ClientLib.get_virtualbox().host.getNetworkAdapter(HostNetworkInterfaceType.HostOnly)

		machine.lockMachine(ClientLib.get_virtualbox().session, 0)
		session = ClientLib.get_virtualbox().session
		#session.console.add_host_only_network
