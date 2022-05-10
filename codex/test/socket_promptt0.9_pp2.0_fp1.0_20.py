import socket
# Test socket.if_indextoname()
(hname, aliases, ipaddrs) = socket.gethostbyaddr('8.8.8.8')
(pname, port) = socket.getservbyport(53, 'tcp')
(pname, port) = socket.getservbyport(53, 'udp')
ifi_name = socket.if_indextoname(1)
(ifi_index, ifi_flags, ifi_mtu, if_type, ifi_name) = socket.if_nameindex()
(ifr_name, ifr_flags, sockaddr) = socket.if_nameindex()
# Test socket.if_index()
(ifr_name, ifr_flags, sockaddr) = socket.if_nameindex()
save_sockaddr = sockaddr
(sockaddr_type, sa_data_1, sa_data_2, sa_data_3, sa_data_4) = socket.sockaddr
(ip_addr, port) = socket.sockaddr
