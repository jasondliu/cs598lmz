import socket
# Test socket.if_indextoname()
indextoname = socket.if_indextoname(1)
print(indextoname)
# Test socket.if_indextoname()
indextoname = socket.if_indextoname(2)
print(indextoname)
# Test socket.if_indextoname()
indextoname = socket.if_indextoname(3)
print(indextoname)
# Test socket.if_indextoname()
indextoname = socket.if_indextoname(4)
print(indextoname)
"""
"""
# Test socket.if_nameindex()
ifnameindex = socket.if_nameindex()
print(ifnameindex)
"""
"""
# Test socket.if_nameindex()
ifnameindex = socket.if_nameindex()
for index, name in ifnameindex:
    print('The index of interface %s is %s' % (name, index))
"""
"""
# Test socket.gethostbyname()
host_addr = socket.gethostbyname('www.b
