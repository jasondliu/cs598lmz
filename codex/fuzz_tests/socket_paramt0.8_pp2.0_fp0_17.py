import socket
socket.if_indextoname(3)

# create a raw datagram socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
# set the socket to receive packets from all interfaces
s.bind(('', 0))
# enable multicasting
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)
# set the multicast interface to be the current interface
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(socket.gethostbyname(socket.gethostname())))
# set the multicast time-to-live to 10
s.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 10)
# join the group
s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(GROUP_ADDR) + socket.inet_aton(socket.gethostbyname(socket.
