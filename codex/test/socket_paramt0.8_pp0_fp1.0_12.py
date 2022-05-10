import socket
socket.if_indextoname(2)
#网卡的识别码是2，因此返回了‘eth1:’ ，
socket.if_nameindex()
#返回了[(1, 'lo'), (2, 'eth1')] 。
'''

# 3.2 获取本机IP地址
'''
