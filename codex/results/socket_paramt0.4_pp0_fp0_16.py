import socket
socket.if_indextoname(3)

#扫描某个网段的主机
from scapy.all import *

def arp_monitor_callback(pkt):
    if ARP in pkt and pkt[ARP].op in (1,2):
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")

sniff(prn=arp_monitor_callback, filter="arp", store=0)

#获取网络接口
from scapy.all import *
conf.iface = "eth0"

#获取网络接口
from scapy.all import *
conf.iface = "eth0"

#获取网络接口
from scapy.all import *
conf.iface = "eth0"

#获取网络接口
from scapy.all import *
conf.iface
