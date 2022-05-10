import socket
# Test socket.if_indextoname()

# Test the function
print(socket.if_indextoname(1))

# Test with an invalid index
try:
    print(socket.if_indextoname(0))
except socket.error as err:
    print("Caught an error:", err)
