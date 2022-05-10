import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:').
#	To build in memory database into readable file, do 
#		open('/tmp/file.db','wb').write(':memory:'.encode() + con.iterdump().encode())

# To get output (STDOUT, STDERR etc) in copyable and clickable CLI, see:
#	https://www.lesstif.com/pages/viewpage.action?pageId=1758026

# To redirect all logs to both stdout and handlers, set
#		logger.propagate = True
# To prevent logging if is not set, see: https://docs.python.org/2/howto/logging.html#library-config
# To get current level of root logger:
#		logging.getLogger().getEffectiveLevel()
# To set environment variable, do:
#		import os; os.putenv('VARIABLE','value')

__version__ = '0.1.0'

logger = logging.getLogger('myapp')
hdlr = logging.StreamHandler()
