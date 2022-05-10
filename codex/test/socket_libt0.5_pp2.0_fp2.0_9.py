import socket
import time
import threading
import random
import os
import signal
import sys

# def handler(signum, frame):
# 	print 'Signal handler called with signal', signum
# 	raise IOError("Couldn't open device!")

# signal.signal(signal.SIGALRM, handler)

# signal.alarm(5)

# try:
#     f = open('/dev/ttyS0')
#     print f.read()
#     f.close()
# except IOError:
#     print 'Got IOError'

# signal.alarm(0)

# sys.exit()

# try:
# 	f = open('/dev/ttyS0')
# 	print f.read()
# 	f.close()
# except IOError:
# 	print 'Got IOError'

# sys.exit()

# f = open('/dev/ttyS0')
# print f.read()
# f.close()

# def handler(signum, frame):
#    
