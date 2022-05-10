import select
# Test select.select
import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.listen(1)

c, addr = s.accept()

# Wait until a socket is readable
r, w, e = select.select([c], [], [], 1)
print(r)

# Wait until a socket is writable
r, w, e = select.select([], [c], [], 1)
print(w)

# Wait until a socket is either readable or writable
r, w, e = select.select([c], [c], [], 1)
print(r, w)

assert False, "select should have returned!"

# Test select.poll
import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 0))
s.listen(1)

c, addr = s.accept()

# Wait
