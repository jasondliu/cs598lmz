import select
# Test select.select
assert select.select([], [], [], 2) == ([], [], [])
assert select.select([], [], []) == ([], [], [])

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',0))
s.listen(socket.SOMAXCONN)
assert select.select([], [], [], 2) == ([], [], [])
r, w, x = select.select([s],[],[], 2)
assert r == [s]
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8080))
# Blocking in select for bad sockets not supported.
try:
    r, w, x = select.select([], [s], [], 2)
except TypeError:
    pass
else:
    assert 0, 'Expected a TypeError'

##
# Test polling and epoll.
##

try:
    import select
