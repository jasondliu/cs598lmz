import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.bind(('eth0', 0))

# Construct the packet.
ip = IP(src='192.168.0.1', dst='192.168.0.2')
tcp = TCP(sport=1234, dport=80)
payload = 'GET / HTTP/1.0\r\n\r\n'
pkt = ip/tcp/payload

# Send the packet.
s.sendto(str(pkt), ('192.168.0.2', 0))
