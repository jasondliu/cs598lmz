import socket
# Test socket.if_indextoname()


print('Testing socket.if_indextoname():')
print('\nSocket with AF_INET')
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('\tLoopback index:', s.if_nametoindex('lo'))
print('\tLoopback name:', s.if_indextoname(1))
print('\tLoopback name with bad index:', s.if_indextoname(99999))
print('\tNon-loopback index:', s.if_nametoindex('en0'))
print('\tNon-loopback name:', s.if_indextoname(2))
print('\tNon-loopback name with bad index:', s.if_indextoname(99999))

print('\nSocket with AF_INET6')
s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
print('\tLoopback index:', s.if_nametoindex('lo0'))
