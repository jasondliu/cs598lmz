import socket
socket.if_indextoname(1)

# socket.if_indextoname(1)
# 'en0'

# socket.if_indextoname(2)
# 'en1'

# socket.if_indextoname(3)
# 'en2'

# socket.if_indextoname(4)
# 'en3'

# socket.if_indextoname(5)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 514, in if_indextoname
#     raise ValueError('invalid interface index')
# ValueError: invalid interface index

# socket.if_indextoname(1)
# 'en0'

# socket.if_indextoname(2)
# 'en1'

# socket.if_indextoname(3)
# 'en2'

# socket.if_indexton
