import socket
# Test socket.if_indextoname() as function
addr1 = socket.if_indextoname(1)
addr2 = socket.if_indextoname(2)
# Print out the results
print(addr1)
print(addr2)
# Test socket.if_indextoname() as method
Addr1 = socket.socket().if_indextoname(1)
Addr2 = socket.socket().if_indextoname(2)
# Print out the results
print(Addr1)
