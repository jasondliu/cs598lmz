import socket
socket.if_indextoname(13)

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.bind(('192.168.1.11',0))
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

while True:
    raw_buffer = s.recvfrom(65565)
    
    print(type(raw_buffer))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    a=1
