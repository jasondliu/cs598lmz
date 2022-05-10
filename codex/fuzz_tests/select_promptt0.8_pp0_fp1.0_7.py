import select
# Test select.select() on an invalid file descriptor.
import array
import os
import sys
import time
import fcntl
import socket
import signal
# Setup pipes.
pipe1, pipe2 = os.pipe()
print('pipe1', pipe1)
print('pipe2', pipe2)
# Setup poll object.
p = select.poll()
print('p', p)
p.register(pipe1, select.POLLIN)
# Setup socketpair.
#sock1, sock2 = socket.socketpair()
#print('sock1', sock1)
#print('sock2', sock2)
p.register(sock1, select.POLLIN)
# Set nonblocking flag.
fd = pipe1
fl = fcntl.fcntl(fd, fcntl.F_GETFL)
print('fl', fl)
fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
# Close one end of pipe.
os.close(pipe2)
# test select POLLIN |
