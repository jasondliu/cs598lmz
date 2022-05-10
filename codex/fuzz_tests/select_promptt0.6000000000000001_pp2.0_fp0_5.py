import select
# Test select.select with timeout in seconds instead of millisecond
# and with timeout not None.

from test import support

# XXX: This test uses time.sleep() and must run in a thread.
support.requires('test_thread')

try:
    select.select([], [], [], 0)
except ValueError:
    raise support.TestFailed('select.select does not support timeout in seconds')

def monitor(readfds, writefds, errorfds, timeout=1.0):
    # Wait for something to happen or timeout to elapse.
    r, w, e = select.select(readfds, writefds, errorfds, timeout)
    if not (r or w or e):
        raise support.TestFailed('select.select timed out')


if __name__ == '__main__':
    support.run_unittest(__name__)
