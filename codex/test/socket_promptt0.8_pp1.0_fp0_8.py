import socket
# Test socket.if_indextoname() and socket.if_nametoindex()
#
# Verify that the output format is e.g. b'eth1' or b'lo' and not
# just an integer or string representation of an integer.

socket.if_indextoname(0)
socket.if_nametoindex(b'lo')

# Verify that the exceptions raised by netdb.h are matched.
import netdb
import sys
def show(exc, *args):
    v = exc(*args)
    print(v.__name__, v)

show(netdb.gaierror, -2, b'name or service not known')
show(netdb.gaierror, -5, b'no address associated with hostname')
show(netdb.gaierror, -8, b'nodename nor servname provided, or not known')
show(netdb.gaierror, -11, b'try again')
show(netdb.herror, -1, b'host not found')
show(netdb.herror, -2, b'no address associated with name')


