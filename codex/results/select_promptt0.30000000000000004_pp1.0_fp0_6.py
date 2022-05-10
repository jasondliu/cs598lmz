import select
# Test select.select()

# select.select() takes three lists of file descriptors:
#   - the first is a list of file descriptors to check for being ready for reading
#   - the second is a list of file descriptors to check for being ready for writing
#   - the third is a list of file descriptors to check for errors
#
# It returns three lists:
#   - the first is a list of file descriptors ready for reading
#   - the second is a list of file descriptors ready for writing
#   - the third is a list of file descriptors with errors
#
# The lists are empty if no file descriptors are ready.
#
# select.select() blocks until at least one file descriptor is ready.
#
# select.select() can be interrupted by a signal (e.g. SIGINT).
# In this case, select.select() returns three empty lists.
#
# select.select() can also have a timeout.
# If the timeout is reached before any file descriptors are ready,
# select.select() returns three empty lists.
#
# select.select() can be called with an empty list
