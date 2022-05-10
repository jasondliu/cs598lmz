import socket
socket.if_indextoname(1)
</code>
The result is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
socket.error: (19, 'No such device')
</code>
I have found that this function is not implemented for Windows.
Is there any other way to convert an interface index to interface name?
I have found that in Python 2.7 there is a function <code>if_nameindex</code> which returns a list of tuples. 
Is there any way to get the same result in Python 3?


A:

You can use the <code>if_nameindex</code> function from the <code>ctypes</code> library.
<code>&gt;&gt;&gt; from ctypes import *
&gt;&gt;&gt; libc = cdll.msvcrt
&gt;&gt;&gt; libc.if_nameindex()
(c_void_p(0), c_void_p(0))
&gt;&gt;&
