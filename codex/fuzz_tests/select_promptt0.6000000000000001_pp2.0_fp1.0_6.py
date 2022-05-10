import select
# Test select.select() with a file descriptor that is closed
# before it is added to the polling list.
#
# This test is expected to fail on Windows because Windows does
# not support select() on non-socket file descriptors.

fd = os.open('/dev/null', os.O_RDONLY)
os.close(fd)

try:
    select.select([fd], [], [])
except ValueError:
    pass
else:
    raise RuntimeError('expected ValueError')
