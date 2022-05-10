import socket
socket.if_indextoname(socket.if_nametoindex('eth0'))
</code>
<blockquote>
<p>'eth0'</p>
</blockquote>
On the other hand, when I tried the same in python3, I got the following error.
<blockquote>
<p>Traceback (most recent call last):   File "", line 1, in
  
      s = socket.if_indextoname(socket.if_nametoindex('eth0')) AttributeError: module 'socket' has no attribute 'if_indextoname'</p>
</blockquote>
I need to find the index of a network interface from its name in python3. Any help is appreciated.


A:

The <code>if_indextoname()</code> and <code>if_nametoindex()</code> functions were added in Python 3.4, see PEP 3144.

