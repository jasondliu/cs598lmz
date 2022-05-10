import select
# Test select.select()

# 1. We can use select.select() to check if the socket is ready for reading
# or for writing.
# 2. It takes a list of sockets to check and returns a list of sockets
# that are ready.

# 1. Create a socket and connect to it.
# 2. Make it non-blocking.
# 3. Pass it to select.select().
# 4. If it’s in the list of readable sockets, read it.
# 5. If it’s in the list of writable sockets, write to it.
# 6. If it’s in the list of exceptional sockets, handle the exception.

# We’ll use the simpler version of select.select() that takes only three
# lists of sockets to check.


# ########################
# Creating a non-blocking socket
# ########################

# The first step is to create a non-blocking socket.
# You can do this by passing the socket.SOCK_NONBLOCK flag to socket.socket().
# A non-blocking socket will return immediately when there is no data available.

import socket
