import select
# Test select.select()
# select.select() returns 3 lists of file descriptors.
#
# The first list is the file descriptors that are ready for read
# The second list is the file descriptors that are ready for write
# The third list is the file descriptors with exceptions (not needed)

# The third list is always empty. Because this is a simple client,
# we are only interested in the first list.
#
# select.select() takes three lists of file descriptors to monitor.
# If a file descriptor is in the first list, it is monitored for
# readability. If a file descriptor is in the second list, it is
# monitored for writability.
#
# If a file descriptor is in both lists, it means that it will be
# monitored for both readability and writability.
#
# select.select() returns the three lists of file descriptors.
# The first list is the file descriptors that are ready for read
# The second list is the file descriptors that are ready for write
# The third list is the file descriptors with exceptions (not needed)
#
# The third list is always empty. Because this
