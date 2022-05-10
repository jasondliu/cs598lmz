import socket
# Test socket.if_indextoname()

try:
    socket.if_indextoname(0)
except socket.error:
    print('socket.if_indextoname() does not work')
    sys.exit(0)

# Try to get the name of a non-existing interface
try:
    socket.if_indextoname(1)
except socket.error as e:
    print(e.args)
    sys.exit(0)

print('socket.if_indextoname() works')
sys.exit(1)
