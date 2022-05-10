import select
# Test select.select()

# select.select() takes three lists of file descriptors and waits until
# some of them are ready for some kind of I/O.
# The first list is the list of file descriptors to be checked for being
# ready to read.
# The second list is the list of file descriptors to be checked for being
# ready to write.
# The third list is the list of file descriptors to be checked for error
# conditions.
# The return value is a triple of lists of file descriptors: subsets of the
# first three arguments.
# The first list returned contains the subset of the first argument, the
# second list returned contains the subset of the second argument, and the
# third list returned contains the subset of the third argument.
# The first list returned contains the file descriptors that are ready to
# read, the second list returned contains the file descriptors that are ready
# to write, and the third list returned contains the file descriptors that
# have an exceptional condition pending.
# The return value is a triple of lists of file descriptors.
# The first list returned contains the file descriptors that are ready to
#
