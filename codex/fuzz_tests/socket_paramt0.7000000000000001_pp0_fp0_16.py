import socket
socket.if_indextoname('1')

interface = scapy.all.get_if_list()[0]
mac = scapy.all.get_if_hwaddr(interface)

# set up the socket
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))
s.bind((interface, 0))

# send the packet
s.send(scapy.all.Ether(src=mac, dst="ff:ff:ff:ff:ff:ff")/scapy.all.ARP(op=2, psrc="10.0.2.4", pdst="10.0.2.1")/scapy.all.Padding(load="X" * 18))

# get the response
data = s.recv(1024)

# parse the packet
pkt = scapy.all.Ether(data)

# print the result
print(pkt.show())

# close the socket
s.close()
 
```

```
In [1]: runfile('/home/
