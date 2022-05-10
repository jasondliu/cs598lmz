import select
# Test select.select()

# select.select() takes 3 lists of file descriptors as arguments.
# The first list is the list of file descriptors to be monitored for
# being ready to read. The second list is the list of file descriptors
# to be monitored for being ready to write. The third list is the list
# of file descriptors to be monitored for errors.

# select.select() returns 3 lists. The first list contains the file
# descriptors that are ready to read. The second list contains the
# file descriptors that are ready to write. The third list contains
# the file descriptors that have errors.

# select.select() will block until one of the file descriptors in the
# first list is ready to read, one of the file descriptors in the
# second list is ready to write, or one of the file descriptors in the
# third list has an error.

# select.select() will return the lists of file descriptors that are
# ready to read, ready to write, and have errors.

# select.select() will return an empty list if the timeout is reached
# and none of the file descriptors
