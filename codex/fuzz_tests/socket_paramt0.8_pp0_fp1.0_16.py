import socket
socket.if_indextoname(3)
</code>
But it returns me:
<code>socket.error: [Errno 19] No such device
</code>
How can I get Wifi Interface name ?


A:

Use the <code>netifaces</code> module:
<code>import netifaces
print(netifaces.interfaces())
</code>
This will print the names of all interfaces. To get the WiFi interface you'll probably have to check the other attributes (like <code>netifaces.ifaddresses</code>, or look through the docs).

