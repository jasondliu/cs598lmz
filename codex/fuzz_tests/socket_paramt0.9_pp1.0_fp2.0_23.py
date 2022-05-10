import socket
socket.if_indextoname(socket.if_nametoindex(b'lo'))
sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
sock.bind(('lo', 3))
sock.send(b'h')
sock.recv(1024)
pkt = IP(dst='127.0.0.1')/TCP(dport=[22,23],flags='S')
ans,unans = sr(pkt,multi=True)
ans.nsummary(prn= lambda (s,r): r.sprintf("%IP.src% is alive"))
pkt.show()
pkt[layers.tcp].flags
pkt[layers.tcp].haslayer(layers.tcp.flags)
pkt[layers.tcp].haslayer(layers.tcp)
pkt[layers.tcp].haslayer(layers.tcp.RST)
TCP(dport=[22,23],flags='S')
IP(dst='127.0.0.1')/TCP(d
