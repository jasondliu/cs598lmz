import socket
socket.if_indextoname(10)
</code>
The error traceback is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
OSError: [Errno 19] No such device
</code>
I've also tried:
<code>sudo apt-get install python3-dev
</code>
But the error persists.
How do I fix this?


A:

You need to run the python interpreter as root.
<code>sudo python3
</code>

