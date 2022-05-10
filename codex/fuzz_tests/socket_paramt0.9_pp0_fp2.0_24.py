import socket
socket.if_indextoname(30)
socket.gethostname()
</code>
and for ip4
<code>import socket
socket.inet_ntoa(struct.pack('L', socket.INADDR_ANY))
</code>

