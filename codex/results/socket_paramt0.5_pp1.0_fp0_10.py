import socket
socket.if_indextoname(3)
</code>
but it always returns:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 19] No such device
</code>
I also tried to use <code>socket.if_nameindex()</code> to get all the interfaces, but it returns an empty list.
I am using python 2.7.6

