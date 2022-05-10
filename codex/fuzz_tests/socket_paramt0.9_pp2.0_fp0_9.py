import socket
socket.if_indextoname(10)
</code>
I've searched and searched and tried different things, and while there is info online, it's not very straightforward. Is there simple way to do this?


A:

You may wish to try the following:
<code>import psutil
import netifaces as ni

iface = psutil.net_if_addrs()["en0"]
ipv4 = ni.ifaddresses(iface.name)[ni.AF_INET]

for nic in lan:
    if nic.ip == ipv4:
        print(nic.name)
</code>

