import socket
# Test socket.if_indextoname()
print("[Test socket.if_indextoname]")
try:
    print(socket.if_indextoname(1))
except Exception as e:
    print("Error: %s" % e)
print("[Test socket.if_indextoname End]")

# Test socket.if_nameindex()
print("[Test socket.if_nameindex]")
try:
    print(socket.if_nameindex())
except Exception as e:
    print("Error: %s" % e)
print("[Test socket.if_nameindex End]")

# Test socket.if_nametoindex()
print("[Test socket.if_nametoindex]")
try:
    print(socket.if_nametoindex("lo"))
except Exception as e:
    print("Error: %s" % e)
print("[Test socket.if_nametoindex End]")

# Test socket.setblocking()
print("[Test socket.setblocking]")
