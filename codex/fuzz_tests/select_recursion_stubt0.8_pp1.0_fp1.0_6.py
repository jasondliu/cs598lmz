import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    while True:
        r, w, e = select.select([F()], a, a)

def test_closed_fd_select():
    import os
    import time
    # Issue #9791: select() should not treat closed file descriptors as
    # exceptional.
    for fname in ("/dev/null", "/dev/random"):
        try:
            os.stat(fname)
        except OSError as e:
            if e.errno == errno.ENOENT:
                continue
        for flag in xrange(256):
            fd = os.open(fname, os.O_RDONLY)
            try:
                os.close(fd)
                start = time.time()
                r = select.select([fd], [fd], [fd], 5)
                delay = time.time() - start
                # Delay shouldn't be ridiculous even if fd is treated
                # as exceptional.
                # XXX is there a way to be more exact here?
                assert delay < 0.1, "%s: unexpected
