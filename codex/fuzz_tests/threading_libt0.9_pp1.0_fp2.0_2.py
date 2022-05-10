import threading
threading.stack_size(2**25)

from fwk import common,fwk 
from fwk.mng import *

#==================================================================
# logging
#
COMMON = common.Common()
LOGGER = log.GetLogger(COMMON, COMMON.Logfile)
print "....", COMMON.Logfile
#==================================================================
#
#==================================================================
#
class TCPClient(object):
	"""Docstring for TCPClient"""
	def __init__(self, logger=None, port=None, ms_server=None, ms_with=None ):
		self.logger = logger
		self.PORT = port
		self.cnt = 0
		self.ms_server = ms_server
		self.ms_with = ms_with
		self.tcps = None
		self.my = {}
		self.rec = []
		#===================================================
		#

		self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.__sock
