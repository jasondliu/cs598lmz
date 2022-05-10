import select
# Test select.select()

# select.select() takes 3 lists of file descriptors as arguments.
# The first list is the list of file descriptors to be monitored for
# being ready to read.
# The second list is the list of file descriptors to be monitored for
# being ready to write.
# The third list is the list of file descriptors to be monitored for
# having an error condition.

# select.select() returns 3 lists of file descriptors.
# The first list is the list of file descriptors that are ready to read.
# The second list is the list of file descriptors that are ready to write.
# The third list is the list of file descriptors that have an error condition.

# select.select() blocks until at least one of the file descriptors in
# the first list is ready to read, or at least one of the file descriptors
# in the second list is ready to write, or at least one of the file
# descriptors in the third list has an error condition.

# select.select() can also be used to monitor a single file descriptor
# for being ready to read, or for being ready to write
