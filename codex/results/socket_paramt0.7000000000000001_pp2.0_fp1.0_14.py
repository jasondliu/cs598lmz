import socket
socket.if_indextoname()
</code>
The first result is:
<code>'lo'
</code>
The second result is:
<code>'wlan0'
</code>
How can I get the second result?


A:

You could use the <code>socket.if_indextoname</code> and <code>socket.if_nametoindex</code> functions.
<code>&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.if_indextoname(1)
'lo'
&gt;&gt;&gt; socket.if_indextoname(2)
'eth0'
&gt;&gt;&gt; socket.if_nametoindex('lo')
1
&gt;&gt;&gt; socket.if_nametoindex('eth0')
2
</code>

