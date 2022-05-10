import socket
socket.if_indextoname(1)

import struct
struct.unpack('9s',b'\x01\xa0\xc2')

import fcntl

fcntl.ioctl(fd,name,request,arg)

在这里，可以使用socket.socket()函数创建一个新的socket文件描述符，然后使用fcntl.ioctl()函数请求SIOCGIFFLAGS（2）操作。在这里，第一个参数还是网络接口索引，第二个参数是c_uint32类型。我们把常量项struct.pack()函数输入一个元组。由于这个函
