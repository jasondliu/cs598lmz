import select
# Test select.select on a list of sockets.
# This test is not exhaustive.
import select
import socket
import time

def test(readable, writable, exceptable, timeout=None):
    readable, writable, exceptable = select.select(readable, writable,
                                                   exceptable, timeout)
    print 'readable      =', readable
    print 'writable      =', writable
    print 'exceptable    =', exceptable

port = 50007

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', port))
server.listen(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', port))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect(('localhost', port))

test([sock], [], [])
test([sock], [], [], 0.1)
test([], [], [])
test([],
