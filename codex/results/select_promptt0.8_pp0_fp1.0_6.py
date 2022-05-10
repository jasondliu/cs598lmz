import select
# Test select.select() and select.poll() for
# interrupted system calls.

def run_select_on(fd, ev):
    # select.select() doesn't raise EINTR for me, under Red Hat 8
    # (kernel 2.4.18-14) nor under FreeBSD 4.5.
    # Select on read and write, and see which one gets ready.
    r, w, x = select.select([fd], [fd], [])
    if ev == select.POLLIN and fd not in r:
        print "select.select() didn't show fd %d ready for reading, but it should have" % fd
    elif ev == select.POLLOUT and fd not in w:
        print "select.select() didn't show fd %d ready for writing, but it should have" % fd
    else:
        print "select.select() on fd %d behaved as expected" % fd

def run_poll_on(fd, ev):
    # select.poll() raises EINTR.
    p = select.poll()
    p.register(fd,
