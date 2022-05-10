import select
# Test select.select

# Create a pair of connected sockets
s1, s2 = socket.socketpair()

# Create a pair of connected sockets
s3, s4 = socket.socketpair()

# Create a pair of connected sockets
s5, s6 = socket.socketpair()

print('Sockets pairs up')
for s in s1, s2, s3, s4, s5, s6:
    s.setblocking(0)

print('Beginning the select')

# Wait for at least one of the sockets to be ready for processing
# A 3-timeout is used, so after 3 seconds the loop will end
# even if none of the connected sockets are ready.

# The select call is a blocking call; it will not return until
# at least one of the sockets is ready for processing.

# The select call returns 3 lists of socket objects.
# The first list contains the sockets that are ready for reading.
# The second list contains the sockets that are ready for writing.
# The third list contains sockets that have raised exceptions.
# The timeout value is included so that the select call will not block
#
