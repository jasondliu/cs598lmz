import select
# Test select.select()

# select.select() takes 3 lists as arguments.
# The first list contains the objects to be checked for being readable.
# The second list contains the objects to be checked for being writable.
# The third list contains the objects to be checked for having an exceptional condition.

# The return value is a tuple of three lists containing the subset of the passed objects that are ready.
# The first list contains the objects that are ready for reading.
# The second list contains the objects that are ready for writing.
# The third list contains the objects that have an exceptional condition (e.g. out-of-band data).

# select.select() is a blocking call.
# If the timeout is omitted it will block until at least one file descriptor is ready.
# A timeout of zero specifies a poll and never blocks.

# select.select() is available on all platforms.
# However, it supports only file descriptors on Unix and Windows.
# On Windows, it can also be used with sockets.

# select.select() is a useful tool for monitoring multiple file descriptors.
# However, it is not very efficient.
# On Unix
