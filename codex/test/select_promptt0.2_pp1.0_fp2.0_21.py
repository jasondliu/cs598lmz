import select
# Test select.select()

# select.select() takes three lists of file descriptors:
#   - the first list is the list of file descriptors to check for being ready for reading
#   - the second list is the list of file descriptors to check for being ready for writing
#   - the third list is the list of file descriptors to check for errors
#
# select.select() returns three lists of file descriptors:
#   - the first list is the list of file descriptors ready for reading
#   - the second list is the list of file descriptors ready for writing
#   - the third list is the list of file descriptors with errors
#
# select.select() takes a timeout parameter, which is the maximum time to wait for any file descriptors to become ready.
#   - if timeout is None, select.select() blocks until at least one file descriptor is ready
#   - if timeout is 0, select.select() returns immediately, even if no file descriptors are ready
#   - if timeout is > 0, select.select() blocks for up to timeout seconds, or until at least one file descriptor is ready
#
# select.select()
