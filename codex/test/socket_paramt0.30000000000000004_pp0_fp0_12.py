import socket
socket.if_indextoname(3)

# 'en0'

# The if_indextoname() function returns the name of the interface with the given index.
# The index is the value returned by if_nametoindex() or if_nametoindex_ex().
# If the index is not valid, an exception is raised.

# The if_indextoname() function is available on all platforms.
# On Windows, the if_indextoname() function is only available on Windows Vista and later.

# The if_indextoname() function is not thread-safe:
# it is not safe to call it simultaneously from multiple threads.
# This function is also not reentrant:
# it is not safe to call it from a signal handler that interrupted a previous call to this function.

# Changed in version 3.5: On Windows, the if_indextoname() function is now available on Windows Vista and later.

# Changed in version 3.7: On Windows, the if_indextoname() function is now thread-safe.
