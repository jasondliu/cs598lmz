import socket
socket.if_indextoname(19)
</code>
but I get this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'if_indextoname'
</code>
I checked the attribute and it exists on my machine and I've already imported it from socket module.


A:

Try calling the function on the <code>socket</code> object. 
<code>import socket
s = socket.socket()
s.if_indextoname(19)
</code>

