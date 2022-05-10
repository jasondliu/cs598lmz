import socket
socket.if_indextoname(3)
</code>
and the output I got was-
<code>'en1'
</code>
But when I try to get the MAC address of this interface using <code>gethostbyname</code>, it gives me the IP address instead of MAC address.
<code>socket.gethostbyname('en1')
</code>
output-
<code>'&lt;the IPv4 address of my PC&gt;'
</code>
I am using python 2.7.13 on Mac OS Sierra and don't want to use any third party library for this.

