import weakref
#import threading
import logging
import time

#import thread
import threading
#from thread import *
import time
import sys

log = logging.getLogger(__name__)

# Log the position of the bug
class ThreadClass(threading.Thread):
	def __init__(self, view, world, i):
		"""
		Threads to handle the bug.
		"""
		threading.Thread.__init__(self)
		self.daemon = True
		self.view = weakref.ref(view)
		self.world = weakref.ref(world)
		self.i = i

	def run(self):
		"""
		Run the thread.
		"""
		log.debug("Starting %s ..." % self.i)		
		self.view().log_position(self.i, self.world().b[self.i].get_position())		
		log.debug("%s DONE!" % self.i)		
	

