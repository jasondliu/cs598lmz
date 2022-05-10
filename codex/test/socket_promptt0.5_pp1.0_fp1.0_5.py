import socket
# Test socket.if_indextoname

import support
support.compileJPythonc("test183c.py", core=1, jar="test183.jar", output="test183.err")

import test183c

