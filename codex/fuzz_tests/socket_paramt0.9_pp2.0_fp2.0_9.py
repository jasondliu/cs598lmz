import socket
socket.if_indextoname(1)
//    'en4'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.sendto(b'hello', ('127.0.0.1', 8880))
sock.recv(8)
//    'hello'


//socket.socketpair()
//    创建一个套接字对，所谓套接字对就是两个紧密相关的套接字，有些系统对套接字对的实现支持不够，比如windows，这种情况下，会调用失败。
//
//    此函数特别使用socketpair()函数，函数
