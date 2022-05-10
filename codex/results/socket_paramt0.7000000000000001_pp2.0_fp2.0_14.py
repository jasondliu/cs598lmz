import socket
socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE))
</code>
(I don't know whether that's a Python 3.2 or even 3.3 feature.)

