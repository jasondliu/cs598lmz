import socket
socket.if_indextoname(3)

Returns the interface name from the specified index number.

In [202]: socket.if_indextoname(2)
Out[202]: 'en1'
'''


'''
socket.getaddrinfo(host, port,
                   family=0, type=0, proto=0, flags=0)

                   它是一个万能的函数，能够返回所有类型的地址信息。
                   member, value
                   family  ->  AF_INET
                   type    ->  SOCK_STREAM / SOCK_DGRAM
                   proto   ->  IPPROTO_TCP / IPPROTO_UDP / IPPROTO_IP
                   proto和type是对应的。


In [204]: socket.getaddrinfo('www.python.org', 'http')
Out[204]:
[(<AddressFamily.AF_INET6: 10>,
  <SocketKind.SOCK_STREAM: 1>,

