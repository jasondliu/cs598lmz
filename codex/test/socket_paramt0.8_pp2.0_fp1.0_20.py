import socket
socket.if_indextoname()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostbyname('www.google.com'),80))

mreq = struct.pack("=4sl", socket.inet_aton("224.0.0.251"), socket.INADDR_ANY)

s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)



while True:
    data, addr = s.recvfrom(1024)
