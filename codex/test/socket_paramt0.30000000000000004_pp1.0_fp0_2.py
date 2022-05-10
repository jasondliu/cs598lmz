import socket
socket.if_indextoname(3)

socket.if_nametoindex('en0')

socket.gethostbyname('www.python.org')

socket.gethostbyname_ex('www.python.org')

socket.gethostbyaddr('93.184.216.34')

socket.gethostname()

socket.getfqdn()

socket.getnameinfo(('93.184.216.34', 80), 0)

socket.getnameinfo(('93.184.216.34', 80), socket.NI_NUMERICHOST)

socket.getnameinfo(('93.184.216.34', 80), socket.NI_NUMERICSERV)

socket.getnameinfo(('93.184.216.34', 80), socket.NI_NOFQDN)

socket.getnameinfo(('93.184.216.34', 80), socket.NI_NAMEREQD)

socket.getnameinfo(('93.184.216.34', 80), socket.NI_DGRAM)

