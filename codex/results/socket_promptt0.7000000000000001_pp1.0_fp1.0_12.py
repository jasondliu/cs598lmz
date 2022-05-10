import socket
# Test socket.if_indextoname()
print('\nsocket.if_indextoname()')
import socket
print('{}'.format(socket.if_indextoname(1)))

# Test socket.if_nametoindex()
print('\nsocket.if_nametoindex()')
import socket
print('{}'.format(socket.if_nametoindex('lo')))

# Test socket.if_nameindex()
print('\nsocket.if_nameindex()')
import socket
print('{}'.format(socket.if_nameindex()))

# Test socket.gethostbyname()
print('\nsocket.gethostbyname()')
import socket
print('{}'.format(socket.gethostbyname('localhost')))

# Test socket.gethostbyname_ex()
print('\nsocket.gethostbyname_ex()')
import socket
print('{}'.format(socket.gethostbyname_ex('localhost')))

# Test socket.gethostbyaddr()
print('\nsocket.gethostbyaddr()')
import socket
print('
