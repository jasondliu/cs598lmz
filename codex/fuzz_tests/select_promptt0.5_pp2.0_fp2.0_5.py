import select
# Test select.select()
#
# select.select() is a function that can wait for a file descriptor to become
# readable or writable, or to have an exception condition.
#
# This function is very useful when you want to wait on multiple file
# descriptors.
#
# Here is a simple example:
#
#   import select
#
#   r, w, e = select.select([socketA], [socketB], [], 10)
#
#   if r:
#     # socketA is readable
#   elif w:
#     # socketB is writable
#   else:
#     # no socket is ready, so sleep for 10 seconds
#
# The first three arguments to select.select() are three lists of file
# descriptors to wait on.  The fourth argument is the timeout, in seconds.
#
# The return value is a tuple of three lists.  The first list contains the
# file descriptors that are readable.  The second list contains the file
# descriptors that are writable.  The third list contains the file descriptors
# that have an exception condition.
#
# If
