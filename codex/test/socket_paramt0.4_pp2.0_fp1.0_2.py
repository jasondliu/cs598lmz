import socket
socket.if_indextoname(3)

# 'en0'

socket.if_indextoname(4)

# 'en1'

# The if_indextoname() function takes an integer index and returns the network interface name corresponding to that index.

# The if_nameindex() function returns a list of tuples containing the integer index and the interface name for all interfaces.

socket.if_nameindex()

# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]

# The if_nametoindex() function is the reverse of if_indextoname(), taking a string interface name and returning the corresponding integer index.

socket.if_nametoindex('en0')

# 4

# The if_nameindex() and if_nametoindex() functions are available on all platforms. The if_indextoname() function is available on Windows, Mac OS X, and Linux.

# The
