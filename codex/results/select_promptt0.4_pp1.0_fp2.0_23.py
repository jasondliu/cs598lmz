import select
# Test select.select()
#
# This is a simple test to ensure that select.select() works correctly.
# It is not intended to be a full test of the module.
#
# The test works by creating a pair of connected sockets, then calling
# select() with a timeout of zero.  The sockets are then closed and
# the test checks that select() returned the expected values.
#
# The test is repeated with each combination of the following:
# - socket type: SOCK_STREAM, SOCK_DGRAM
# - timeout: zero, non-zero
# - socket state: readable, writable, both
# - socket direction: in, out, both
#
# If any of the tests fail, the test prints an error message and exits
# with a non-zero exit code.
#
# The test is also run with a timeout of None.  This is to ensure that
# select() does not hang indefinitely when given an infinite timeout.
#
# The test is also run with a timeout of -1.  This is to ensure that
# select() does not hang indefinitely when given an infinite timeout.
#
# The test is
