import socket
socket.if_indextoname(i)
</code>
But in python3 it doesn't return a string.
How can I do that in python3 ?


A:

I'm not sure why you're getting a <code>bytes</code> object back in Python 3. This is what I get:
<code>&gt;&gt;&gt; import socket
&gt;&gt;&gt; i = socket.if_nametoindex("lo")
&gt;&gt;&gt; socket.if_indextoname(i)
'lo'
</code>
You can always decode the bytes object using whatever encoding you prefer:
<code>&gt;&gt;&gt; socket.if_indextoname(i).decode("utf8")
'lo'
</code>
If you want to know what the return type of <code>if_indextoname</code> is, you can use the <code>type(...)</code> function:
<code>&gt;&gt;&gt; type(socket.if_indextoname(i))
&lt;class 'str'&
