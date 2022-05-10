import socket
socket.if_indextoname(14)
 
'en0'

socket.if_nameindex()
 
[(1, 'lo0'),
 (2, 'gif0'),
 (3, 'stf0'),
 (4, 'en0'),
 (5, 'en1'),
 (6, 'fw0'),
 (7, 'en2'),
 (8, 'en3'),
 (9, 'en4'),
 (10, 'en5'),
 (11, 'en6'),
 (12, 'en7'),
 (13, 'en8'),
 (14, 'bridge0')]

socket.if_nametoindex('en0')
 
4

# Hack Windows to support this.

if hasattr(socket, 'if_nameindex'):
    print('Function if_nameindex exists')
else:
    print('Function if_nameindex does not exist')

Function if_nameindex does not exist

# Hack Windows to support this.

socket.if_nameindex()
 
Traceback (most recent call last):
  File "<pyshell#30>", line
