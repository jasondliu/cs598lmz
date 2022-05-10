import socket
# Test socket.if_indextoname

to_find = socket.if_indextoname(1)
print("Testing socket.if_indextoname(1) -> '%s'" % to_find)

if to_find == 'lo':
    print("PASSED")
else:
    print("FAILED")
