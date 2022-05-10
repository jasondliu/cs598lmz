import socket
socket.if_indextoname(1)

# if_indextoname(index)
# Return the name of an interface, given its index.

# On Windows, this function only accepts integers and raises ValueError if the index is not recognized.

# On other systems, this function accepts either integers or strings, and if a string is passed, the function interprets it as the name of an interface, and returns the corresponding index.

# Changed in version 3.3: On Windows, this function only accepts integers.

# New in version 3.3: On other systems, this function accepts either integers or strings.

# Changed in version 3.5: On Windows, this function now raises OSError instead of WindowsError.

# Changed in version 3.6: On Windows, this function now raises ValueError instead of OSError.
