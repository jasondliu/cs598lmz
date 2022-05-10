import socket
socket.if_indextoname(5)

#On Linux machines, this will most probably fail because the X server uses the first Ethernet interface. If you have more than
#one network interface, entering the following command tells you how many interface are available: 
socket.if_nameindex()


#sends common UDP data
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = 'all work and no play makes jack a dull boy\n'.encode()
s.sendto(data*100000, ('127.0.0.1', 1234))



#receives UDP broadcast
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 1234))
data, addr = s.recvfrom(1024)
print(data)
