import socket
socket.if_indextoname('3')

#Trace at the module level
import cStringIO as StringIO
from trace import CoverageResults
import sys
sys.path.insert(0, '../modules')
coverage = CoverageResults()
coverage.start()

from my_bad_module import *
fr
