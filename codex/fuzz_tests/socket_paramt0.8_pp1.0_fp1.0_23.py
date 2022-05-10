import socket
socket.if_indextoname('12')

# this works on my 64bit Debian:
&gt;&gt;&gt; socket.if_indextoname(3)
'eth0'
</code>
No idea how to get this in Windows though.

