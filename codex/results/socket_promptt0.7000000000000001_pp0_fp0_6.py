import socket
# Test socket.if_indextoname()
import sys, os, array
# Test os.environb, os.getenvb()
import struct
# Test struct.pack()
import errno
# Test errno.EINTR

def test(condition, message):
    if not condition:
        print "Test failed:", message
        sys.exit(1)
    else:
        print "Test succeeded:"

# Test exec
try:
    exec '1+1'
except SyntaxError:
    print 'exec: SyntaxError exception caught as expected'
else:
    test(False, "exec: SyntaxError exception expected but not caught")

# Test string encoding
u = unicode('abc', 'iso-8859-1')
u2 = unicode(u, 'ascii')
test(u == u2, "Error in unicode encoding (1)")

s = u.encode('utf-8')
u3 = unicode(s, 'utf-8')
test(u == u3, "Error in unicode encoding (2)")

# Check that PyArg_Parse
