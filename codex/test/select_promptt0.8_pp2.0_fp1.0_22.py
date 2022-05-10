import select
# Test select.select() on all file descriptors

# This currently tests on stdin, stdout, and stderr.
# Later we will generalize it to test on any file descriptor.
#
# This does not test select()'s behavior on sockets.
fd_sets = map(lambda x: x[0], select.select([0], [1], [2], 1.0))
