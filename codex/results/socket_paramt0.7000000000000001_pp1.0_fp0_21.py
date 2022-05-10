import socket
socket.if_indextoname(0)

socket.gethostbyname('localhost')
socket.gethostbyname_ex('localhost')
socket.gethostbyaddr('127.0.0.1')

socket.getfqdn("127.0.0.1")
socket.getfqdn("localhost")

socket.gethostname()
socket.gethostbyname(socket.gethostname())

socket.getprotobyname("ip")
socket.getservbyname("http", "tcp")
socket.getservbyport(80, "tcp")

socket.ntohs(0x1234)
socket.ntohl(0x1234)
socket.ntohl(0x12345678)
socket.ntohs(0x1234)

socket.htons(0x1234)
socket.htonl(0x1234)
socket.htonl(0x12345678)
socket.htons(0x1234)

socket.setdefaulttimeout(10)
socket.getdefaulttimeout()

socket.getaddrinfo("www.python.
