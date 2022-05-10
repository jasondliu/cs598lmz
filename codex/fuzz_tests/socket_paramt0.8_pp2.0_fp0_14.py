import socket
socket.if_indextoname(3)

# 192.168.2.101
# socket.gethostbyaddr('192.168.2.101')


# for k,v in socket.if_nameindex():
#     print(socket.if_indextoname(k),v)



# print([(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
