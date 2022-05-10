import socket
socket.if_indextoname(2)

# If a socket is created with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
# then the IP headers can be provided by the user.

# If a socket is created with socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
# then the Ethernet headers can be provided by the user.

# If a socket is created with socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
# then the Ethernet headers can be provided by the user and the IP headers must be provided by the user
# and the TCP, UDP, or ICMP headers must be provided by the user.

# If a socket is created with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
# then the IP headers can be provided by the user and the TCP headers must be provided by the user.

# If a socket is created with socket.socket(socket.AF_INET, socket.SOCK_
