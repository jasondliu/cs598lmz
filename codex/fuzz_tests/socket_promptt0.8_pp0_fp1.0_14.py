import socket
# Test socket.if_indextoname().
print("if_indextoname(1) =", socket.if_indextoname(1))
print("if_indextoname(1, 'foo') =", socket.if_indextoname(1, 'foo'))
print("if_indextoname(1, b'foo') =", socket.if_indextoname(1, b'foo'))

try:
    print("if_indextoname(1, bytearray(2)) =", socket.if_indextoname(1, bytearray(2)));
except:
    print("if_indextoname(1, bytearray(2)) =", sys.exc_info()[1])

try:
    print("if_indextoname(1, ()) =", socket.if_indextoname(1, ()));
except:
    print("if_indextoname(1, ()) =", sys.exc_info()[1])

try:
    print("if_indextoname(1, object()) =", socket.
