import select
# Test select.select()

# create non-blocking pipe
r1, w1 = os.pipe()
r2, w2 = os.pipe()

# mark both pipes as non-blocking
for fd in (r1, r2, w1, w2):
    fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

# create a few sockets
s1 = socket.socket()
s1.setblocking(0)
s1.bind(('localhost', 1729))
s1.listen(1)
s2 = socket.socket()
s2.setblocking(0)
s2.bind(('localhost', 1730))
s2.listen(1)
