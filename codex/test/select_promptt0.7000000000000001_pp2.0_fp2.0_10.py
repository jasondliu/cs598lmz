import select
# Test select.select to wait for a socket to become available.
#
# This is a test, not a demo.
#
# Send a message to the socket, but don't close it.  By the time select
# returns, it should be ready to receive.

import socket
import select

print('Opening socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',0))
s.listen(1)
s.setblocking(0)

print('Sending message')
s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_client.connect(s.getsockname())
s_client.send(b"Hello")

print('Waiting for socket')
r,w,e = select.select([s],[],[],5.0)
if not (r or w or e):
    print('Timed out')
else:
    print('Got something')
    assert r
    s_server,addr = s.accept()
