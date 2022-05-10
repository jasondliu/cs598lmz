import select
# Test select.select()

# select.select() takes 3 lists of file descriptors
# and waits until one or more of the descriptors are ready for some kind of I/O
# The first list is the list of descriptors to be checked for being readable
# The second list is the list of descriptors to be checked for being writable
# The third list is the list of descriptors to be checked for errors
# The return value is a tuple of three lists of file descriptors that are ready
# for reading, writing and errors respectively

# The function returns immediately if any of the three lists is non-empty
# and at least one of the descriptors in the list is ready
# Otherwise, the function blocks until some descriptors become ready

# The function can also be told to block for a given maximum time
# before returning

# Example:
# Suppose you have a server that serves both as a normal server
# and as an inetd-style server
# The server would have a main loop that looks like this:

while True:
    # Perform a select on the sockets that the server is listening to
    # This will block until a client connects to the
