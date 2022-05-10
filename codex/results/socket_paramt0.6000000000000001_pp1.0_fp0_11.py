import socket
socket.if_indextoname(1)

# socket.error: (99, 'Cannot assign requested address')
</code>
What is this error and how can it be fixed?
I am on OSX 10.9.5.


A:

This error means that the index you're providing to <code>if_indextoname</code> doesn't exist.
<code>&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.if_indextoname(1)
'lo0'
&gt;&gt;&gt; socket.if_indextoname(2)
'lo0'
&gt;&gt;&gt; socket.if_indextoname(3)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
socket.error: (99, 'Cannot assign requested address')
</code>
If you run <code>ifconfig</code> you should see the interfaces you have:
<code>&gt;&gt;&gt; import sub
