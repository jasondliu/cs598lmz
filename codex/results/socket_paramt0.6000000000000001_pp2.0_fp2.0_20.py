import socket
socket.if_indextoname(2)

#After that, we can get the corresponding IP address
socket.gethostbyname("en0")

#The getaddrinfo() method translates the host name into an IP address
socket.getaddrinfo("www.python.org", 80)

#The getnameinfo() method gets the host name and service for a sockaddr
socket.getnameinfo(("127.0.0.1", 80), 0)

#The gethostname() method gets the host name
socket.gethostname()

#The gethostbyaddr() method gets the host name by IP address
socket.gethostbyaddr("127.0.0.1")

#The getservbyname() method gets the service associated with a port
socket.getservbyname("ftp")

#The getservbyport() method gets the service associated with a port
socket.getservbyport(80)

#The getprotobyname() method gets the protocol associated with a service
socket.getprotobyname("tcp")
