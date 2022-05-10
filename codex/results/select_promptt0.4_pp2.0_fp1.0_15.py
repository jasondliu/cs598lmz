import select
# Test select.select
print 'Testing select.select...',
sys.stdout.flush()

# Test select.select
# XXX This test is not very good.  It doesn't check that the right
# XXX descriptors are ready, it just uses the first ready descriptor.
# XXX It should really check that all the descriptors it uses are ready
# XXX for the right operation.

# Create two pipes and an event
r1, w1 = os.pipe()
r2, w2 = os.pipe()
e = threading.Event()

# Create non-blocking pipes
for fd in (r1, r2, w1, w2):
    fl = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# Create a thread that waits for the event.  When the event is set,
# it closes w1 and w2.
def trigger():
    e.wait()
    os.close(w1)

