import socket
socket.if_indextoname(3)

#'en0'

socket.gethostbyname('www.python.org')

#'82.94.164.162'

socket.gethostbyname_ex('www.python.org')

#('www.python.org', [], ['82.94.164.162'])

socket.gethostbyaddr('82.94.164.162')

#('www.python.org', [], ['82.94.164.162'])

socket.getnameinfo(('82.94.164.162', 80), 0)

#('www.python.org', 'http')

socket.getnameinfo(('82.94.164.162', 80), socket.NI_NUMERICHOST)

#('82.94.164.162', '80')

socket.getnameinfo(('82.94.164.162', 80), socket.NI_NUMERICSERV)

#('82.94.164.162', '80')

