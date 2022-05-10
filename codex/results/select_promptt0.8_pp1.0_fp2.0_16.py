import select
# Test select.select()

import socket, sys, select, Queue

#
# (1) Create sockets
#

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_sock.bind(('127.0.0.1', 12345))
tcp_sock.listen(128)
udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
udp_sock.bind(('127.0.0.1', 12345))
epoll = select.epoll()
epoll.register(tcp_sock.fileno(), select.EPOLLIN)
epoll.register(udp_sock.fileno(), select.EPOLLIN)

#
# (2)
