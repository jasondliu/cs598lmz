import signal
# Test signal.setitimer()
import sys
import time
import traceback

import lib_util
import lib_common

from sources_types.CIM_ManagedElement import CIM_ManagedElement as survol_CIM_ManagedElement

# This is the time in seconds between two refreshes.
# However, it could be very long, unless the user refreshes the browser.
# This timer will be started by the client.
DefaultRefreshDelay = 60

# This is the time in seconds before the server should send a refresh to the client.
# If the user does not refresh the client, it will refresh automatically after this delay.
# This timer will be started by the server.
DefaultRefreshToClientDelay = 3

class Test_Timer(object):

	# Without this, the server would be terminated by a signal.SIGALRM
	def __init__(self):
		self.alarm_flag = False

	def signal_handler(self, signum, frame):
		self.alarm_flag = True

	def alarm_handler(self, signum, frame):
		self.al
