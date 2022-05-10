import socket
# Test socket.if_indextoname

import support
support.compileJPythonc("test183c.py", core=1, jar="test183.jar", output="test183.err")

import test183c

try:
    print test183c.getInterfaceName(1)
except socket.error, e:
    print "Exception: ", e
try:
    print test183c.getInterfaceName(2)
except socket.error, e:
    print "Exception: ", e
try:
    print test183c.getInterfaceName(3)
except socket.error, e:
    print "Exception: ", e
try:
    print test183c.getInterfaceName(4)
except socket.error, e:
    print "Exception: ", e

# The next test is commented out because it fails on Windows.
#print test183c.getInterfaceName(5)
