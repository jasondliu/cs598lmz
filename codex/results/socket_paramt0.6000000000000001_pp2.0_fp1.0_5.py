import socket
socket.if_indextoname()
</code>
And this is the error I get:
<code>Traceback (most recent call last):
  File "C:\Users\Daniel\Desktop\socket.py", line 1, in &lt;module&gt;
    import socket
  File "C:\Users\Daniel\Desktop\socket.py", line 2, in &lt;module&gt;
    socket.if_indextoname()
AttributeError: module 'socket' has no attribute 'if_indextoname'
</code>
I also tried importing <code>netifaces</code> but I get the same error.


A:

You should not name your own module <code>socket.py</code> because it will shadow the standard library module.

