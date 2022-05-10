import socket
# Test socket.if_indextoname
print(socket.if_indextoname(1))
print(socket.if_indextoname(1,""))
try:print(socket.if_indextoname(1,None))
except TypeError:pass
else:print("should have raised TypeError")
# Test socket.if_nameindex
print(socket.if_nameindex())
# Test socket.if_nameindex with an invalid parameter
try:print(socket.if_nameindex(""))
except TypeError:pass
# Test socket.if_nameindex with a valid parameter
print(socket.if_nameindex("en0"))
# Test socket.if_nametoindex
print(socket.if_nametoindex("en0"))
# Test socket.if_nametoindex with an invalid parameter
try:print(socket.if_nametoindex(""))
except ValueError:pass

# Test socket.accept
try:import usocket as socket
except ImportError:pass
import socketserver
# Test TCPServer
