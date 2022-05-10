import select
# Test select.select()

# Windows only

# Test data: a list of sockets
sockets = [socket.socket() for i in range(3)]

# Define the timeout
timeout = 1

# Test select.select()
rlist, wlist, xlist = select.select(sockets, sockets, sockets, timeout)
print(rlist)
print(wlist)
