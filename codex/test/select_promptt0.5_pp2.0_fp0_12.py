import select
# Test select.select()
#
# This test checks that select.select() does not crash when given
# a file descriptor that is not a socket.
#
# This test is needed because the implementation of select.select()
# in the Python standard library uses the FD_SET() macro from the
# Windows API, which does not support non-socket file descriptors.
#
# The FD_SET() macro is not supported on Cygwin, so the test is skipped
# on Cygwin.

try:
    fd = os.open(os.path.abspath(__file__), os.O_RDONLY)
except (AttributeError, OSError):
    # os.open() is not supported
    raise unittest.SkipTest("os.open() is not supported")

try:
    select.select([fd], [], [])
finally:
    os.close(fd)
