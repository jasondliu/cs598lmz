import socket
# Test socket.if_indextoname(char* ifr_name) function

#test socket.if_indextoname(int ifr_index)
print("Name of index 10: ", socket.if_indextoname(10))
