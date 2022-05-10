import select
# Test select.select() and select.poll() for
# interrupted system calls.

def run_select_on(fd, ev):
    # select.select() doesn't raise EINTR for me, under Red Hat 8
    # (kernel 2.4.18-14) nor under FreeBSD 4.5.
    # Select on read and write, and see which one gets ready.
    r, w, x = select.select([fd], [fd], [])
