import mmap
# Test mmap.mmap(-1, 1024)
#
# When mmap.mmap(-1, length) is called, the function calls
# mmap.mmap(None, length) which will use the default file descriptor
# of -1 (stdin).  However, on Windows, the default file descriptor
# is 0 (stdout).  This is an issue because the file descriptor is
# used as the handle for the mapping.  The handle will be 0 which
# is a valid handle.  The call to mmap.mmap(0, length) will return
# a valid mapping object.
#
# The issue is that the file descriptor is never closed.  The
# mapping object will be created, but the the file descriptor will
# be closed when the object is destroyed.  If the file descriptor
# is 0, the stdout file descriptor will be closed.
#
# This test checks for this issue by creating a mmap object with
# a file descriptor of -1.  It then checks to see if the file
# descriptor is 0.  If the file descriptor is 0, the test fails.
#
# If the test fails, the stdout file
