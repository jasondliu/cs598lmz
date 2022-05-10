import socket
# Test socket.if_indextoname()
import subprocess
# Test subprocess.Popen()
import sys
# Test sys.exit()
import time
# Test time.sleep()
import traceback
# Test traceback.print_exc()
import unittest
# Test unittest.main()

# Import the necesary modules from the project
from network_functions import *
from network_classes import *
from network_globals import *

class Test_network_functions(unittest.TestCase):
	""" Unit tests for the network_functions module. """

	def test_check_ip_address(self):
		""" Test the check_ip_address function.
		"""

		# Test a valid IP address
		self.assertTrue(check_ip_address("192.168.1.1"))
		self.assertTrue(check_ip_address("192.168.1.1/24"))

		# Test an invalid IP address
