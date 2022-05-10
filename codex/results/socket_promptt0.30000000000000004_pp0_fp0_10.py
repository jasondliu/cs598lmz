import socket
# Test socket.if_indextoname()

# Test with invalid arguments
try:
    socket.if_indextoname(1, "")
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    socket.if_indextoname(1)
except TypeError:
    pass
else:
    print("TypeError not raised")

try:
    socket.if_indextoname()
except TypeError:
    pass
else:
    print("TypeError not raised")

# Test with valid arguments
print(socket.if_indextoname(1))
