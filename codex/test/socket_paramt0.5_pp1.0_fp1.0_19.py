import socket
socket.if_indextoname(3)

# get by if_index
socket.if_nameindex()

# get by if_name
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
socket.if_nametoindex(s.getsockname()[0])

# get by if_name
socket.if_nameinfo(s.getsockname(), socket.NI_NUMERICHOST)

# get by if_name
socket.if_nameinfo(s.getsockname(), socket.NI_NUMERICSERV)

# get by if_name
socket.if_nameinfo(s.getsockname(), 0)

# get by if_name
socket.if_nameinfo(s.getsockname(), socket.NI_NOFQDN)

# get by if_name
socket.if_nameinfo(s.getsockname(), socket.NI_DGRAM)

# get by if_name
