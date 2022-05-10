import socket
socket.if_indextoname(ifindex)
</code>
http://docs.python.org/2/library/socket.html#socket.if_indextoname
The problem is the interface is not a standard one, and the index does not exist in /sys/class/net/.
What can I do in this situation?

