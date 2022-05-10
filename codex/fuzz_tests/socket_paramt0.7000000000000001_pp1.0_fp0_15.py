import socket
socket.if_indextoname(3)

socket.ntohs(0x1234)
socket.ntohl(0x12345678)
socket.htons(0x1234)
socket.htonl(0x12345678)

socket.inet_aton('192.168.0.2')
socket.inet_ntoa(b'\xc0\xa8\x00\x02')

socket.inet_pton(socket.AF_INET, '192.168.0.2')
socket.inet_pton(socket.AF_INET6, '3ffe:8311:ffff:1234:5678:9abc:def0:1111')
socket.inet_ntop(socket.AF_INET, b'\xc0\xa8\x00\x02')
socket.inet_ntop(socket.AF_INET6, b'\x3f\xfe\x83\x11\xff\xff\x12\x34\x56\x78\x9a\xbc\xde\xf0\x11\x11')

socket.getaddr
