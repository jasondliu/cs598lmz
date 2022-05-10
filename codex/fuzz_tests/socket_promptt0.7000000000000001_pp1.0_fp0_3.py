import socket
# Test socket.if_indextoname(3)

from test_support import verbose, TestFailed

if_names = socket.if_indextoname(3)

if verbose:
    print 'The name of the interface corresponding to index 3 is', if_names

if if_names != "lo":
    raise TestFailed(
            'if_indextoname(3) should return "lo" not "%s"' % if_names)
from socket import *
import time
import os

if verbose:
    print '\n*** Testing basic socket interface'

# Create a server socket
if verbose:
    print 'Creating server socket'
serversock = socket(AF_INET, SOCK_STREAM)

# Bind the socket to a port
if verbose:
    print 'Binding it to a port (this may take a while)...'
serversock.bind(("localhost", 0))

port = serversock.getsockname()[1]

# Start listening
if verbose:
    print 'Listening...'
serversock.listen(5)


