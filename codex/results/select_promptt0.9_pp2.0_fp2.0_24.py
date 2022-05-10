import select
# Test select.select()

# I/O multi-plexing: one thread can now monitor the data
# on a number of different file descriptors (a socket
# waiting for connections, a socket that is connected
# to a client, a pipe waiting for input from a subprocess
# started by the server, and standard input).write())

# Wait for input on any of the registered file descriptors.
# The first three arguments are sequences of file descriptors
# to be waited for: rlist -- wait until ready for reading;
# wlist -- wait until ready for writing; xlist -- wait
# for an ``exceptional condition'' (see the manual page
# for what your system considers such a condition).
# The fourth argument specifies a timeout in seconds; it
# may be omitted or given as None to specify an unbounded wait.
# The return value is a tuple of three lists corresponding
# to the first three arguments; each contains the subset
# of the corresponding file descriptors that are ready.
# (The exception info for the exceptional condition file descriptors
# are simply returned as a tuple instead.)

# Transfer data between sockets and file-like objects:

