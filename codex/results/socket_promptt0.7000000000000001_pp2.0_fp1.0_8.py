import socket
# Test socket.if_indextoname

import support
support.compileJPythonc("test315c.py", output="test315.err")

import test315m

if test315m.socket.if_indextoname(1) != 'lo':
    raise support.TestError('if_indextoname() returns wrong interface')
