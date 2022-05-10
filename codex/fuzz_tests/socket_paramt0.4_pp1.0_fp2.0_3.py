import socket
socket.if_indextoname(0)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/lib/python2.7/socket.py", line 449, in if_indextoname
    return _socket.if_indextoname(interface)
socket.error: [Errno 22] Invalid argument
</code>
I am running OSX 10.8.5.
What is the problem?


A:

The problem was that the interface was not up.

