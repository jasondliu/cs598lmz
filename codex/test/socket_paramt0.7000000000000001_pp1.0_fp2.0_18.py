import socket
socket.if_indextoname(3)

import scapy.all as scapy

for i in range(3,4):
    print(scapy.arch.Windows.iflist[i].ifname)
    print(scapy.arch.Windows.iflist[i].name)
    print(scapy.arch.Windows.iflist[i].pcap_name)
    print(scapy.arch.Windows.iflist[i].guid)
    print(scapy.arch.Windows.iflist[i].ipaddr)
    print(scapy.arch.Windows.iflist[i].netmask)
    print(scapy.arch.Windows.iflist[i].hwaddr)
    print(scapy.arch.Windows.iflist[i].mtu)
    print(scapy.arch.Windows.iflist[i].description)
    print("--------------------------------------------------------------------")

print(scapy.arch.Windows.iflist)
a = scapy.arch.Windows.iflist[1].guid
print(a.split('-')[-1])
print(type(a))
