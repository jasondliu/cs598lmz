import threading
# Test threading daemon
import time
import os
import subprocess
import sys
import signal

class Threading_Daemon(threading.Thread):
	"""
	This class represents a Threading_Daemon object. This class is responsible for running the daemon that listens to the user's commands and executes them.
	"""
	def __init__(self, logger, config, queue):
		threading.Thread.__init__(self)
		self.logger = logger
		self.config = config
		self.queue = queue
		self.daemon_thread = None

	# Daemon thread
	def run(self):
		self.logger.info("Threading Daemon running...")
		self.logger.info("Current process ID: %d" % os.getpid())
		self.logger.info("Current thread ID: %d" % threading.get_ident())
		self.logger.info("Current thread name: %s" % threading.current_thread().name)

		# Get the command name from the config file
		command = self
