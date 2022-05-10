import socket
socket.if_indextoname('0x2')
#'en1'
</code>
But I am not able to find the way to get the interface index from the interface name.
Is it possible?


A:

There is no 1-1 mapping between interface names and interface indices.  If you have a list of names, you can look up the corresponding index using <code>if_nametoindex()</code>.  The only way to get a list of names is to first enumerate the indices using <code>if_nameindex()</code>.

