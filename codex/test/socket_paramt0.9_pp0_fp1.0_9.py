import socket
socket.if_indextoname(46)

'''
网络基础

'''

#获得网络接口信息
#关于hostname 和 计算机IP地址的对应关系,可以通过socket.gethostbyname()来获得计算机的IP地址
print(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))


#使用linux命令ifconfig来查看当前的网络接口
#inet addr:10.10.10.100 Bcast:10.10.10.255 Mask:255.255.255.0
#inet6 addr: fe80::b2a3:176e:8a1a:9ec/64 Scope:Link
#UP BROADCAST RUNNING MULTICAST MT
