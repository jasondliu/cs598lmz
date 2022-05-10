import socket
socket.if_indextoname(10)
</code>
But I am not sure how to access the network interfaces in the first place.


A:

You can get the list of all interfaces using <code>netifaces</code> module:
<code>&gt;&gt;&gt; import netifaces
&gt;&gt;&gt; netifaces.interfaces()
['lo', 'eth0', 'eth1', 'eth2', 'eth3', 'docker0']
</code>
And then you can get their corresponding <code>index</code> using <code>netifaces.if_nametoindex</code>:
<code>&gt;&gt;&gt; netifaces.if_nametoindex('lo')
1
&gt;&gt;&gt; netifaces.if_nametoindex('eth0')
2
&gt;&gt;&gt; netifaces.if_nametoindex('eth1')
3
</code>

