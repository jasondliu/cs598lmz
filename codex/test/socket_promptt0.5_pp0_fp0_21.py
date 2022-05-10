import socket
# Test socket.if_indextoname
print( socket.if_indextoname(1) )

import socket
# Test socket.if_nametoindex
print( socket.if_nametoindex("lo") )

# Test socket.getaddrinfo
print( socket.getaddrinfo("www.baidu.com", 80, 0, 0, socket.SOL_TCP) )

# Test socket.getnameinfo
print( socket.getnameinfo(("www.baidu.com", 80), 0) )

# Test socket.gethostbyname
print( socket.gethostbyname("www.baidu.com") )

# Test socket.gethostbyname_ex
print( socket.gethostbyname_ex("www.baidu.com") )

# Test socket.gethostbyaddr
print( socket.gethostbyaddr("127.0.0.1") )

# Test socket.getfqdn
print( socket.getfqdn("www.baidu.com") )

# Test socket.gethostname
print( socket.gethostname() )
