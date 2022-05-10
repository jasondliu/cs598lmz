import select
# Test select.select
print 'Testing select.select ...',
fd_set = select.fd_set([0, 2])
print fd_set.gets(),
fd_set.clear()
print fd_set.gets(),
fd_set.set(6)
print fd_set.gets(),
fd_set.set(3)
print fd_set.gets(),
fd_set.set(1)
print fd_set.gets(),
fd_set.set(9)
print fd_set.gets(),
fd_set.clear(9)
print fd_set.gets(),
fd_set.clear(6)
print fd_set.gets(),
fd_set.set(64)
print fd_set.gets(),
print '.'

# Test select.poll
print 'Testing select.poll ...',
from select import poll
from socket import socket
fds = []
for i in range(8):
    s = socket().fileno()
    fds.append(s)
    poll().register(s, poll.POLLIN)
    for p in
