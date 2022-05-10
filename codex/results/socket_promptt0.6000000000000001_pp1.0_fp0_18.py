import socket
# Test socket.if_indextoname()

# The output is different on different machine
# This test is only used to check if the function
# is available

try:
    socket.if_indextoname(1)
except AttributeError:
    print('SKIP')
    raise SystemExit

print('if_indextoname:', socket.if_indextoname(1))
