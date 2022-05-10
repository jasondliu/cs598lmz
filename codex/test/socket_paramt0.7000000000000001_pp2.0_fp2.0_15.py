import socket
socket.if_indextoname(3)

r = sr1(IP(dst="192.168.0.1")/ICMP())
r.show()

r = sr1(IP(dst="192.168.0.1")/TCP(sport=666, dport=80))
r.show()

r = sr1(IP(dst="192.168.0.1")/UDP(sport=666, dport=53)/DNS(rd=1, qd=DNSQR(qname="www.google.com")))
r.show()

# TCP SYN flood
send(IP(dst="192.168.30.5")/TCP(dport=80, flags="S"))
send(IP(dst="192.168.30.5")/ICMP())
