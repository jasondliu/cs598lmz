import socket
socket.if_indextoname(3)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth0')
</code>
I would like to do the same thing in Python 3.
I have tried the following:
<code>s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 0))
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'eth0')
</code>
but it doesn't work, it says:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 22] Invalid argument
</code>
I have also tried the following:
<code>s = socket.socket(
