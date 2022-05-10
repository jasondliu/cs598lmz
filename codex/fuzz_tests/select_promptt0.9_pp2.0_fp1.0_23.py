import select
# Test select.select vs select.poll.
# For test a, when select returns to a ready file descriptor, it still
# gives it back next time; with poll, the file descriptor was added
# to the return list only once.
# Test b, poll is faster on my linux system, with 500 file descriptors.

# This one exhibits the problem of select.select returning a file descriptor
# as ready that's already been returned; it should not be returned anymore
# unless it becomes ready again.
import random, os, select
fds = []
poll = select.poll()

for i in range(500):
    r, w = os.pipe()
    fds.append(r)
    fds.append(w)
    poll.register(r, select.POLLIN)

ready = {}  # dict from fd to how many times we've read from it
while fds:
    timeout = random.random()
    print "select.select", timeout
    r, w, e = select.select(fds, [], [], timeout)
    for fd in r:
        del ready[fd]

