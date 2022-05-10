import select
# Test select.select()

# The select() call is a way to ask the operating system if any of a set of
# file descriptors is ready for reading, ready for writing, or has an error.
# select() is the most efficient way to wait for one or more file descriptors
# to become ready for I/O.

# select() takes three lists of file descriptors: those that should be checked
# for being ready to read, those that should be checked for being ready to
# write, and those that should be checked for error conditions. The first list
# is passed in as the first argument to select(), the second as the second
# argument, and the third as the third argument.

# select() returns three lists of file descriptors. The first list contains
# the file descriptors that are ready for reading, the second list contains
# the file descriptors that are ready for writing, and the third list contains
# the file descriptors that have errors.

# select() can also take an optional fourth argument, which is a timeout in
# seconds. If the timeout is zero, select() will return immediately. If the
# timeout is less than zero, select
