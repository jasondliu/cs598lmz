import select
# Test select.select()
#
# select.select() returns a list of three lists.  The first list contains
# the file descriptors that are ready for reading.  The second list contains
# the file descriptors that are ready for writing.  The third list contains
# the file descriptors with errors.
#
# The file descriptors that are ready for reading are the file descriptors
# that have data available to be read.  The file descriptors that are ready
# for writing are the file descriptors that can accept data to be written.
#
# The file descriptors that have errors are the file descriptors that have
# had an error occur on them.  The error may be that the file descriptor has
# been closed, or that an error has occurred on the socket.  The error can
# be retrieved with socket.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR).
#
# The file descriptors that are ready for reading, writing, and with errors
# are the file descriptors that are ready for reading, writing, and with
# errors at the time of the call to select.select().  They may not be ready
