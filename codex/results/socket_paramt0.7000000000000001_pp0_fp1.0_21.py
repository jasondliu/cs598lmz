import socket
socket.if_indextoname(socket.SIOCGIFINDEX(socket.if_nametoindex('eth0')))
</code>
However, this does not work for me, as I get a <code>error: [Errno 99] Cannot assign requested address</code> error.
Is there a way to get the interface index for a given interface name on Linux/Windows?


A:

<code>if_indextoname</code> requires an integer index.  If you have the interface name, you can use <code>if_nametoindex</code> to get the index.  If you want the name back, then you can use <code>if_indextoname</code> with the index.

