import socket
# Test socket.if_indextoname()
#
# If the test fails, then the test will segfault.
#
# This test is skipped when running on Windows or when running on a
# system without the if_indextoname() function.

try:
    socket.if_indextoname
except AttributeError:
    raise unittest.SkipTest("if_indextoname not available")

# This test should not be run on Windows.
if sys.platform == 'win32':
    raise unittest.SkipTest("if_indextoname not available on Windows")

# This test should not be run on a system without if_indextoname().
try:
    socket.if_indextoname(1)
except OSError as e:
    if e.errno == errno.EINVAL:
        raise unittest.SkipTest("if_indextoname not available")
    else:
        raise

# Try to find a valid interface index.
