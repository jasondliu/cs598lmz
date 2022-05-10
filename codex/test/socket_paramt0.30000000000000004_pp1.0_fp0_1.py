import socket
socket.if_indextoname(1)

# 'en0'

socket.if_indextoname(2)

# 'lo0'

socket.if_indextoname(3)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid network interface index

socket.if_indextoname(0)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid network interface index

socket.if_indextoname(1)

# 'en0'

socket.if_indextoname(2)

# 'lo0'

socket.if_indextoname(3)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid network interface index

socket.if_indextoname(0)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module
