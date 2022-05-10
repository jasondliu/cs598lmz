import socket
# Test socket.if_indextoname()
print("Test socket.if_indextoname()")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Error: {}".format(socket.error(socket.errno)))

rc = sock.connect_ex(("seclab.cs.ucsb.edu", 80)) 
if rc != 0:
    print("Error: {}".format(socket.error(rc)))
    raise SystemExit

# Get the index and name of the network interface used
# to connect to www.example.com
info = sock.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE)
print("Network device: {}".format(socket.if_indextoname(bin(info)[2:])))
