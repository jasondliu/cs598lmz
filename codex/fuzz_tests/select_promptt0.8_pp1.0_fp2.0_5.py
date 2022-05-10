import select
# Test select.select().

# This is long time-out test.  This can take seconds on platforms where
# select() has poor resolution, such as on IRIX-5.2.  It should run in
# less than a few seconds on any modern Unix.

# Check that there are at least 255 file descriptors available.  We'll
# need a lot of them.
import os

if __name__ == "__main__":
    fds = 256
    while os.dup(0) < fds:
        fds -= 1
    fds -= os.dup(0)
    if fds < 255:
        print("skipped (requires at least 255 file descriptors)")
        import sys; sys.exit(0)

    rfds, wfds, xfds = select.select([0], [], [], 2)
    if not rfds:
        print("skipped (select() didn't give a proper result)")
        import sys; sys.exit(0)

    # Check that select() with a single-bit map works.
    rfds, wf
