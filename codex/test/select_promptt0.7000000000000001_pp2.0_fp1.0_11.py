import select
# Test select.select() in a way that makes sure it's not blocking.
# For example, a possible implementation of select() on Windows
# might return immediately if the timeout is zero, and the fds
# aren't ready.
#
# This test isn't fast, but it doesn't need to be.

r, w = os.pipe()
r2, w2 = os.pipe()

