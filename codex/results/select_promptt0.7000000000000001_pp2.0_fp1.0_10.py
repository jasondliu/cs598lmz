import select
# Test select.select with large FD numbers
# See http://bugs.jython.org/issue2534

# create a bunch of sockets
sockets = []
for i in range(100):
    sockets.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

# select on all the sockets
w, r, x = select.select(sockets, sockets, sockets)

# close all the sockets
for s in sockets:
    s.close()
