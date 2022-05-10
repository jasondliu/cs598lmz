import socket
socket.if_indextoname("1")
</code>


A:

Try executing <code>sudo python</code> or <code>sudo ipython</code>.  The problem is that the <code>if_indextoname</code> interface requires elevated privileges.

