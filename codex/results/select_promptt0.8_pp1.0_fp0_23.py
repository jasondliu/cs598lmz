import select
# Test select.select
import sys

def test(timeout, rfds, wfds, xfds):
    print 'timeout =', timeout
    rs, ws, xs = select.select(rfds, wfds, xfds, timeout)
    print 'rs =', rs
    print 'ws =', ws
    print 'xs =', xs

r, w = os.pipe()

# Create three sockets, connect them, and put them in non-blocking mode.
socks = map(socket.socket, (socket.AF_INET, socket.AF_INET, socket.AF_UNIX))
for s in socks:
    s.setblocking(0)

try:
    s.bind(('<broadcast>', 0))
except socket.error, msg:
    print 'Skipped test: ', msg
else:
    map(s.connect, [('localhost', 80), ('localhost', 20), ('.', 0)])

# The initial values of the rfds and wfds arguments.
rfds = [sys.stdin, r, socks[0
