import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a file descriptor is ready
#
# Return value: three lists of objects that are ready
#
# select.select() is a useful way to multiplex input from multiple sources.
#
# For example, you can use it to wait for input from both a network connection and standard input at the same time.
#
# The following example waits for input from either standard input or a socket.
#
# If the user types a line of text at the terminal, it echos the line back.
#
# If the socket is readable, it accepts a connection and reads a line of text from the socket and echoes it back.
#
# If the socket is not readable, it assumes the connection has been closed and exits.
#
# The example uses a non-blocking socket, so
