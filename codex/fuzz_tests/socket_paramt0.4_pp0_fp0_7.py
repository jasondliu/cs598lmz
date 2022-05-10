import socket
socket.if_indextoname(1)

# 'en0'

# 可以使用 socket.if_nameindex() 函数来获取所有接口名称

socket.if_nameindex()

# [(1, 'lo0'), (2, 'gif0'), (3, 'stf0'), (4, 'en0'), (5, 'en1'), (6, 'fw0'), (7, 'vmnet1'), (8, 'vmnet8')]

# 可以使用 socket.if_nametoindex() 函数来获取指定接口的索引

socket.if_nametoindex('lo0')

# 1

# 可以使用 socket.gethostbyname() 函数来获取主机名对应的 IP 地址

socket.gethostbyname('www.python.org')

#
