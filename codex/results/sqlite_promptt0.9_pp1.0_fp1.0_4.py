import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:", check_same_thread=False)


import striga.server.application, striga.server.service, striga.server.service.pathtool
import striga.server.service.monitor, striga.server.service.monitor.emergeevent, striga.server.service.notification, striga.server.service.staticfile, striga.server.service.dsn
import striga.core.moduleloader, striga.core.exception

###

###

__all__ = ['Main', 'MainThread']

###

class MainThread(striga.service.strigaservice.SchedulerStoppableThread):

	def __init__(self, ctx, loglinecallback = None, password = False):
		super().__init__(name = 'MainThread')

		self.__Password = password

		# Use password to allow control
		if password:
			if self.__Password is False:
				self.__Password = str(random.randint(1, 400000))

		self.
