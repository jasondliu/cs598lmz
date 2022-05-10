import socket
# Test socket.if_indextoname()
import sys
import time
from test import support
from test.support import bigaddr
from test.support.script_helper import assert_python_ok
from test.support.socket_helper import bind_port
from test.support.threading_helper import reap_threads
threading = support.import_module('threading')

HOST = support.HOST

# Filename used for testing
if os.name == 'nt':
    lib_name = 'socket.pyd'
else:
    lib_name = 'socket.so'

if_name = socket.if_indextoname(1)
if os.name == 'nt':
    # On Windows, if_name is a unicode string.
    if_name = if_name.encode('ascii')

if_names = {socket.if_indextoname(i): i for i in range(256)}

if_indices = {i: socket.if_nametoindex(name)
              for i, name in if_names.items()}

if_indices
