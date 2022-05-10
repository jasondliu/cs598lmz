import socket
socket.if_indextoname(2)

'''
interface_name = socket.if_indextoname(2)
print(interface_name)
'''

#find the ip address of the interface
socket.if_nameindex()

'''
interface_name = socket.if_nameindex()
print(interface_name)
'''

#find the interface index of the interface
socket.if_nametoindex('en0')
'''
interface_index = socket.if_nametoindex('en0')
print(interface_index)
'''

'''
#find the ip address of the interface
socket.if_nameindex()
interface_name = socket.if_nameindex()
print(interface_name)
'''
