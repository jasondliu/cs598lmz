import select
# Test select.select()
#
# select.select() takes three lists of file descriptors and waits until
# some of them are ready for some kind of I/O.
#
# The first list is the list of file descriptors to be checked for being
# ready to read.
#
# The second list is the list of file descriptors to be checked for being
# ready to write.
#
# The third list is the list of file descriptors to be checked for error
# conditions.
#
# The return value is a triple of three lists corresponding to the three
# lists of file descriptors.  Each of the three returned lists contains
# only the subset of the corresponding parameter that is ready for the
# corresponding I/O operation.
#
# Note that on Windows, it only works for sockets.
#
# The 'example' directory contains a pair of programs, 'reader' and
# 'writer', that use select() to do I/O on a pair of connected sockets.
#
# This test runs the reader and writer programs as subprocesses.
#
# The parent process creates a pair of connected sockets.  It then
# creates the
