import select
# Test select.select()

docker = get_docker()

# The underlining select() uses the TCP port to decide which FD to return,
# which means we should start a server before we run the test
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 0))
s.listen(1)
ip, port = s.getsockname()

# Note that we must bind to localhost, because Unix connection is not able to
# unblock select()
args = ["python", "-c",
"""
from __future__ import print_function
import socket
import sys
ip, port = sys.argv[1].split(":")
port = int(port)
s = socket.socket()
s.setblocking(1)
s.connect((ip, port))
s.send(b"Hello")
s.close()
""", "%s:%s" % (ip, port)]

docker = get_docker()
c = docker.containers.run
