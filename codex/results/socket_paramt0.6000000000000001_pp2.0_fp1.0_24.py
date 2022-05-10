import socket
socket.if_indextoname(2)

#%%
# socket.getaddrinfo(host, port[, family[, type[, proto[, flags]]]])
# 返回一个元组列表。列表中的每个元组描述一个地址。
# 元组由以下值组成:
# family: 地址族，如socket.AF_INET
# type: 套接字类型，如socket.SOCK_STREAM
# proto: 协议，如0
# canonname: 如果请求的是一个名字（而不是一个地址），这个值是该名字的完全限定版本
# sockaddr: 是
