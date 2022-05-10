import socket
socket.if_indextoname("1")

'eno1'
</code>
<blockquote>
<p>I have the following code:</p>
</blockquote>
<code>netifaces.ifaddresses('eno1')
</code>
<blockquote>
<p>and it returns:</p>
</blockquote>
<code>{18: [{'addr': '00:0c:29:b5:d2:71'}], 2: [{'broadcast': '10.0.0.255', 'netmask': '255.255.255.0', 'addr': '10.0.0.10'}]}
</code>
<blockquote>
<p>I would like to know the proper way of getting the IP Address from the above returned value.</p>
</blockquote>

