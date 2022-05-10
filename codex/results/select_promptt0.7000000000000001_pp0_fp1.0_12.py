import select
# Test select.select() and select.poll() with a large number of
# file descriptors.  (Tested with Linux 2.4.18, glibc 2.2.5.)

import os
import select
import socket
import sys

# How many file descriptors to test with.
try:
    num_fds = int(sys.argv[1])
except (IndexError, ValueError):
    num_fds = 50000

print 'creating', num_fds, 'sockets'
socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(num_fds)]

print 'checking select results'
print '  fds', len(select.select([], [], [], 0)[0])
print '  poll', len(select.poll().poll(0))

print 'connecting sockets'
for s in socks:
    s.connect(('localhost', 80))

print 'checking select results again'
print '  fds', len(select.select([], [], [], 0)[0])
print '
