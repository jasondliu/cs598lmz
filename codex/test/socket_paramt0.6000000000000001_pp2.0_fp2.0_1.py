import socket
socket.if_indextoname(2)

#if_nameindex()-> Returns a list of tuples with interface information
socket.if_nameindex()

#getaddrinfo()-> Translate the hostname to IPv4/v6 address
socket.getaddrinfo('www.google.com', 80)

#gethostbyname()-> Translate a host name to IPv4 address format
socket.gethostbyname('www.google.com')

#create a raw socket and bind it to public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind(('200.200.200.200',0))

# Include IP headers in the captured packets
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a packet
print(s.recvfrom(65565))

# disabled promiscuous mode
