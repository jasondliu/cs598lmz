import socket
socket.if_indextoname(3)

'enp1s0'
</code>
it is not returning any value.
I am using Ubuntu 12.04.


A:

I just tried it on my Mac (which is probably not the same thing as Ubuntu, but should work in the same way):
<code>&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.if_indextoname(1)
'lo0'
</code>
It seems that this only returns the first network interface. I suggest you get a list of all network interfaces and index into that:
<code>&gt;&gt;&gt; import netifaces
&gt;&gt;&gt; netifaces.interfaces()

['lo0', 'en1', 'en0']
</code>
If you want to get the interface which has the IP address you've specified, you can use:
<code>&gt;&gt;&gt; netifaces.ifaddresses('lo0')

{17: [{'addr': 'fe80::1%lo0', 'netmask
