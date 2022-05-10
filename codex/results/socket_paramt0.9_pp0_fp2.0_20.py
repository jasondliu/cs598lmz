import socket
socket.if_indextoname(3)
</code>
On the other hand, my test system (MacOS 10.15.3 with python 3.7.2) worked as expected using the same code.


A:

The number is either the index of the interface stored and returned by <code>if_nameindex()</code>, but many other tools use the traditional <code>if_nametoindex()</code>/<code>if_indextoname()</code> which on Linux can be found in <code>libc</code>.  So, try <code>os.system("ip addr show")</code> and try out some of the interface index returned:
<code>$ ip addr show
1: lo: &lt;LOOPBACK,UP,LOWER_UP&gt; mtu 65536 ...
2: enp60s0: &lt;NO-CARRIER,BROADCAST,MULTICAST,UP&gt; mtu 1500 ...
3: wlo1: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 ...
...
$ python3                      
Python
