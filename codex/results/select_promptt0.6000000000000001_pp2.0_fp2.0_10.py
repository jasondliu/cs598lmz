import select
# Test select.select on dev/null
# The behavior is different on Linux and Solaris, so we handle
# both cases.

def test_select():
    import os
    import time
    if os.name != 'posix':
        return
    fd = os.open('/dev/null', os.O_RDWR)
    try:
        # Wait long enough to make sure we're on a new tick, to
        # avoid a known Linux kernel bug.
        time.sleep(0.01)
        rfd, wfd, xfd = select.select([fd], [], [], 0)
        assert (rfd, wfd, xfd) == ([fd], [], []), (rfd, wfd, xfd)
    finally:
        os.close(fd)

def test_main(verbose=None):
    test_select()

if __name__ == "__main__":
    test_main(verbose=True)
