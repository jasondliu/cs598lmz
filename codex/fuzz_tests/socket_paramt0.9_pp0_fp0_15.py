import socket
socket.if_indextoname("4")

import pcap
pcap.findalldevs()

import subprocess
devnull=open("/dev/null","w")

dev = subprocess.Popen("ip -o link show",shell=True,stdout=subprocess.PIPE,stderr=devnull).communicate()[0]
dev = [ re.match(r"^\d+:\s(?P<interface>.+):.*",i).group("interface") for i in dev.decode().split("\n") if "[NOARP,UP,LOWER_UP]" in i ]
dev.remove("lo")
dev

default_device = dev[0]
default_device

def get_if():
    ifs=pcap.findalldevs()
    iface=None
    for i in ifs:
        if "wlan" in i:
            iface=i
    if not iface:
        print("Cannot find device wlan. Exiting.")
        exit(0)
    return iface
interface=get_if()
default_device
