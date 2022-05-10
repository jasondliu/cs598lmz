import socket
socket.if_indextoname('1')

'''
   说明：
    socket.if_nametoindex(name)
    根据网卡名得到其索引值
    socket.if_indextoname(index)
    根据网卡索引值得到网卡名

'''
socket.if_nametoindex('lo')
socket.if_indextoname(1)
