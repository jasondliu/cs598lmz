import socket
socket.if_indextoname(1)
</code>
and get this error:
<code>socket.error: [Errno 19] No such device
</code>
If i change it to:
<code>import socket
socket.if_indextoname(0)
</code>
I get lo
which i suppose is like loackback?
any ideas why i cant use the higher indexes?


A:

You do actually get the output you expect:
<code>&gt;&gt;&gt; import socket
&gt;&gt;&gt; socket.if_indextoname(2)
'eth0'
&gt;&gt;&gt; socket.if_indextoname(3)
'eth1'
&gt;&gt;&gt; 
</code>

