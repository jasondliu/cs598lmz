import socket
# Test socket.if_indextoname
# Make sure there are interfaces
assert socket.if_indextoname(1)

# Test socket.if_nametoindex
assert socket.if_nametoindex('lo')

def test_import_ssl():
  import ssl

  # This is a minimum test, intended to raise an exception if the
  # SSL module is loaded with no underlying support for SSL at all.
  # An exception may or may not be raised, but the import should
  # definitely go through without a core dump or other disaster.
  ssl.wrap_socket(socket.socket())


# Test struct.unpack
import struct
struct.unpack('>i', b'\x00\x00\x00\x00')

# Test sys.argv
import sys
sys.argv

# Test threading.local
import threading
try:
  import thread
except:
  import dummy_thread as thread

local = threading.local()
local.x = 1
assert local.x == 1

# Test time.clock()
import time
time.clock()

# Test
