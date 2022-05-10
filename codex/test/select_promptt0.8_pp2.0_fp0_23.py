import select
# Test select.select() using a socket pair
import socket
import sys

s1, s2 = socket.socketpair()
s1.setblocking(False)

s1.send(b"hello")
s2.send(b"hello2")

r, w, e = select.select([s1], [s2], [s1, s2], 0.1)
assert r == [s1], r
a
