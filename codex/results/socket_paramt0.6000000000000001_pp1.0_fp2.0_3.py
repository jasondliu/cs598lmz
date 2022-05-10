import socket
socket.if_indextoname('3')

# 'en0'

socket.if_indextoname(3)

# 'en0'

socket.if_nametoindex('lo0')

# 1

socket.if_nametoindex('en0')

# 3

socket.if_nameindex()

# [(1, 'lo0'), (3, 'en0')]

socket.if_nameindex()[0][1]

# 'lo0'

socket.if_nameindex()[1][1]

# 'en0'

import socket
import struct

# On a 64-bit machine, Python 3 will return an int, not a str.
socket.inet_ntop(socket.AF_INET, b'\x7f\x00\x00\x01')

# '127.0.0.1'

socket.inet_pton(socket.AF_INET, '127.0.0.1')

# b'\x7f\x00\x00\x01'

socket.inet_pton(socket
