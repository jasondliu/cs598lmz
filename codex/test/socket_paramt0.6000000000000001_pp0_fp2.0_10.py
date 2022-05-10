import socket
socket.if_indextoname(2)

# 使用if_nameindex获取所有的网络接口
socket.if_nameindex()

# 获取一个网络接口的地址，使用if_nametoindex根据名称获取索引，再使用if_indextoaddr获取地址
socket.if_indextoaddr(socket.if_nametoindex('lo'))

# 获取一个网络接口的netmask，使用if_nametoindex根据名称获取索引，再使用if_indextomask获取netmask
socket.if_indextomask(socket.if_nametoindex('lo'))

# 获取所
