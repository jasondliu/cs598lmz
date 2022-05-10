import select
# Test select.select() with a file descriptor that is not in the right range.
# This used to crash Python.
import os
import sys

# This test is not portable, as it depends on the implementation of select().
# It is known to work on Linux, FreeBSD, and OS X.

# On Linux, select() is implemented using the syscall of the same name.
# The syscall takes three bitmasks of file descriptors, and returns the
# subset of the descriptors that are ready.  The bitmasks are limited to
# the range of file descriptors that the process can open.  (This is
# typically 1024, but can be changed using setrlimit().)
#
# On FreeBSD, select() is implemented using poll(), which is limited to
# OPEN_MAX descriptors.
#
# On OS X, select() is implemented using poll(), which is limited to
# OPEN_MAX descriptors.
#
# On Windows, select() is implemented using WaitForMultipleObjects(),
# which is limited to MAXIMUM_WAIT_OBJECTS handles.  This is typically
# 64.
#
# On
