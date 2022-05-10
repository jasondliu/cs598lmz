import socket
# Test socket.if_indextoname
!./test.sh C3
 
# Nat test.
## Config.
!echo 1 > /proc/sys/net/ipv4/ip_forward
!iptables -t nat -A POSTROUTING -s 192.168.100.0/24 -o eth0 -j MASQUERADE
!iptables -t nat -A PREROUTING -d 10.0.0.2 -j DNAT --to-destination 192.168.100.2
 
## Traffic generation and capture.
!ping -c 2 192.168.100.2 >/dev/null &
!tcpdump -i eth0 -w 1_nat.pcap &
 
## Wait for some time and stop tcpdump.
from time import sleep
sleep(5)
!pkill tcpdump
!./test.sh 1_nat
 
# IPIP test
## Config.
!ip xfrm policy add src 10.0.0.0/24 dst 10.0.0.0/24 dir x src port 2222 tmpl src 192.168.100.2 dst 10.0.
