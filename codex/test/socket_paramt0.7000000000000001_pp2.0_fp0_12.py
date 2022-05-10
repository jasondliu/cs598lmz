import socket
socket.if_indextoname(3)
socket.inet_aton('10.0.0.1')
socket.inet_ntoa(b'\x7f\x00\x00\x01')

# socket.getaddrinfo('www.python.org', '80')
# [
#     (2, 1, 6, '', ('82.94.164.162', 80)),
#     (2, 2, 17, '', ('82.94.164.162', 80)),
#     (2, 3, 0, '', ('82.94.164.162', 80)),
#     (2, 1, 6, '', ('2001:888:2000:d::a2', 80, 0, 0)),
#     (2, 2, 17, '', ('2001:888:2000:d::a2', 80, 0, 0)),
#     (2, 3, 0, '', ('2001:888:2000:d::a2', 80, 0, 0))
# ]

# socket.getnameinfo(('82.94.164.162', 80))
# ('www.python.org', 'http
