import socket
socket.if_indextoname(3)
'p3p1'
socket.if_indextoname(42) # invalid index value
Traceback (most recent call last):
  File "&lt;pyshell#20&gt;", line 1, in &lt;module&gt;
    socket.if_indextoname(42)
socket.error: [Errno 19] No such device
</code>
You'll want to convert interfaces and indexes early and reference them by name for further manipulation. Conversion to and from indexes is extremely fast so there is no real drawback.

