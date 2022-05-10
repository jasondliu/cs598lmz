import socket
# Test socket.if_indextoname

import support
support.compileJPythonc("test148c.py", core=1, jar="test148.jar", output="test148.err")

import test148c

ret = test148c.if_indextoname(socket.if_nametoindex("lo"))
