import socket
# Test socket.if_indextoname
getifaddrs = cdll.LoadLibrary('./libc.so.6').getifaddrs
getifaddrs.restype = c_int
getifaddrs.argtypes = [POINTER(POINTER(ifaddrs))]
freeifaddrs = cdll.LoadLibrary('./libc.so.6').freeifaddrs
freeifaddrs.restype = None
freeifaddrs.argtypes = [POINTER(ifaddrs)]
s = 0
freeaddrinfo = cdll.LoadLibrary('./libc.so.6').freeaddrinfo
freeaddrinfo.restype = None
freeaddrinfo.argtypes = [POINTER(addrinfo)]
getaddrinfo = cdll.LoadLibrary('./libc.so.6').getaddrinfo
getaddrinfo.restype = 4711
getaddrinfo.argtypes = [c_char_p,c_char_p,POINTER(addrinfo),POINTER(POINTER(addrinfo))]

#Create an instance of the C struct
ia = ifaddrs()
