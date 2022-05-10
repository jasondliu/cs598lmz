import socket
socket.if_indextoname(ifindex) # The first parameter is the interface index (1, 2, 3, etc.)
</code>
Above ...
<code>from socket import AF_INET, inet_aton, socket, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.bind(('10.7.7.3', 0))
s.bind(('10.7.7.3', 0))
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.6/socket.py", line 224, in meth
    return getattr(self._sock,name)(*args)
socket.error: address already in use
</code>
Don't launch application on random port. Just launch application on the same socket, no matter what port it is.
Add this to either sysctl.conf (sysctl -p to activate) or /etc/sysctl.d/local.conf:
<code>net.ipv4.ip_local_port_range
