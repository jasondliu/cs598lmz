import socket
socket.if_indextoname(1)
</code>
Then I get:
<code>&gt;&gt;&gt; import socket
socket.if_indextoname(1)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'module' object has no attribute 'if_indextoname'
</code>
I'm using Python 2.7.6 on OS X 10.9.4. 
What am I doing wrong?


A:

In OSX the socket module does not have the <code>if_indextoname</code> function. It is not a bug. If you look at the source code of the Python socket module you'll see that this function is only available on *BSD and Linux systems.

