import socket
# Test socket.if_indextoname for the first 10 interfaces.
for i in range(10):
    try:
        print(socket.if_indextoname(i))
    except Exception as e:
        print("Error:", e)

# Test socket.if_indextoname for an invalid interface.
try:
    print(socket.if_indextoname(99))
except Exception as e:
    print("Error:", e)
