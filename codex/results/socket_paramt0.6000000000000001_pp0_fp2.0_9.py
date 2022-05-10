import socket
socket.if_indextoname(2)
</code>
But that is not what I want, I want to get the name of the interface that is connected to the internet, is it even possible?


A:

You can use the <code>netifaces</code> module to get the interface name and the IP address associated with it:
<code>import netifaces as ni
ni.gateways()['default'][ni.AF_INET][1]
</code>
It returns <code>'eth0'</code> for me.

