import socket
socket.if_indextoname(3)
</code>
However it fails with the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.6/socket.py", line 276, in if_indextoname
    raise error, msg
socket.error: [Errno 22] Invalid argument
</code>
I am using Redhat 6.4. I have no idea what the problem is. Any help would be much appreciated.


A:

It appears that you are using the wrong function.  Try <code>if_indextoname</code> instead.

