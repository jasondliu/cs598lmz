import socket
socket.if_indextoname(2)
</code>
prints <code>lo</code>; this is the loopback interface.
Running on a wireless network, the wireless interface is named <code>wlp1s0</code>, and
<code>&gt;&gt;&gt; import socket
socket.if_indextoname(3)
</code>
prints this.
The other end of the communication is running on a computer with Windows and an ethernet connection.  The ethernet interface is <code>Ethernet</code>, and
<code>&gt;&gt;&gt; import socket
socket.if_indextoname(1)
</code>
prints <code>Ethernet</code>.
However, on the Windows machine, the following code
<code>&gt;&gt;&gt; import socketserver
&gt;&gt;&gt; socketserver.UDPServer(('', 50000), socketserver.BaseRequestHandler).serve_forever()
</code>
fails with
<code>Traceback (most recent call last):
  File "C:\Program Files (x86)\
