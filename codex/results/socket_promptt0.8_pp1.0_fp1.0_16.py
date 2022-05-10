import socket
# Test socket.if_indextoname
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print socket.if_indextoname(s.if_nametoindex('0'))

try:
    print socket.if_indextoname(4294967296)
except socket.error:
    pass
else:
    raise Exception('should raise an exception')
