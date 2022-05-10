import select
# Test select.select performance with no timeouts.
import socket
import time

nsockets = 100
nhandles = nsockets*2
readers = {}
writers = {}
for i in range(nsockets):
    readers[socket.socket()] = None
    writers[socket.socket()] = None
for i in range(600000):
    r, w, e = select.select(readers, writers, [], None)
    #print(len(r), len(w), len(e))

# This is much faster than the C implementation.
# select.poll() is even faster.
