import socket
# Test socket.if_indextoname()

from test_support import verbose
import socket, string

if not hasattr(socket, "if_indextoname"):
    print "socket.if_indextoname() not defined -- test skipped"
    raise SystemExit

if verbose:
    print "if_indextoname(0) ->",
print socket.if_indextoname(0)

if verbose:
    print "if_indextoname(string.lowercase) ->",
print socket.if_indextoname(string.lowercase)
