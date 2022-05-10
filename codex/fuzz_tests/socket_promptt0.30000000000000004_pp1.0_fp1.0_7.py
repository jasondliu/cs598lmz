import socket
# Test socket.if_indextoname()

from test_support import verbose, import_module
import sys

socket = import_module('socket')

if verbose:
    print 'Testing socket.if_indextoname()'

ifname = socket.if_indextoname(1)
if verbose:
    print 'if_indextoname(1) ->', ifname

if ifname != 'lo':
    raise socket.error, 'if_indextoname(1) != "lo"'

ifname = socket.if_indextoname(2)
if verbose:
    print 'if_indextoname(2) ->', ifname

if ifname != 'eth0':
    raise socket.error, 'if_indextoname(2) != "eth0"'

ifname = socket.if_indextoname(3)
if verbose:
    print 'if_indextoname(3) ->', ifname

if ifname != 'sit0':
    raise socket.error, 'if_indextoname(3) != "sit0
