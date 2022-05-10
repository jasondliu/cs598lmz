import socket
socket.if_indextoname(3)
</code>
And I want to get the name of the network interface for a given IP address. I tried to use the <code>socket.gethostbyname_ex</code> method like this:
<code>socket.gethostbyname_ex('192.168.1.1')
</code>
But this method returns only the IP address.
Any idea how to get the network interface name?


A:

You can use <code>ipaddress</code> module to get the appropriate network interface.
<code>import ipaddress
net = ipaddress.ip_network('192.168.1.1')
print(net.interface_name)
</code>
Reference: https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.interface_name

