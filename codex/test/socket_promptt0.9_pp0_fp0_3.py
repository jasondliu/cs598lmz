import socket
# Test socket.if_indextoname
assert socket.if_indextoname(1)

import struct
# Test struct.error
assert struct.error

# Test ssl.OPENSSL_VERSION_INFO
import ssl
assert ssl.OPENSSL_VERSION_INFO

# Test sys.version_info
import sys
assert sys.version_info


import threading
# Just run threading.currentThread() to ensure it's linked properly
threading.currentThread()

import time
# Test time.sleep()
time.sleep(1.0)
time.sleep(0)
time.sleep(1)

# Test time.time()
assert time.time()

# Test time.strptime
time.strptime("30 Nov 00", "%d %b %y")

# Test time.strftime
time.strftime("%d %b %y", (2000,11,30) + (0,) * 6 )
