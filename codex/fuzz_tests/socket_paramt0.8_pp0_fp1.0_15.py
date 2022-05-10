import socket
socket.if_indextoname('1')

# ['lo', 'enp0s3', 'tun0']
</code>
Or you can use <code>psutil.net_if_stats()</code>.
<code>import psutil
print(psutil.net_if_stats())

# 
# lo      : isup=True, duplex=True, speed=10000000, mtu=65536
# eth0    : isup=True, duplex=True, speed=10000000, mtu=1500
# tun0    : isup=True, duplex=True, speed=10000000, mtu=1500
# virbr0  : isup=True, duplex=False, speed=0, mtu=1500
</code>
If you're looking for a full-featured Python network library, <code>netifaces</code> and <code>psutil</code> are perfect.

