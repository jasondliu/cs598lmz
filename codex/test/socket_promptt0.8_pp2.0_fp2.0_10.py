import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(2))
print(socket.if_indextoname(3))
print(socket.if_indextoname(4))
print(socket.if_indextoname(5))
print("Pass" if socket.if_indextoname(1) == "lo" else "Fail")
print("Pass" if socket.if_indextoname(2) == "eth0" else "Fail")
print("Pass" if socket.if_indextoname(3) == "eth1" else "Fail")
print("Pass" if socket.if_indextoname(4) == "eth2" else "Fail")
print("Pass" if socket.if_indextoname(5) == "eth3" else "Fail")

# Test socket.if_nameindex
print(socket.if_nameindex())
