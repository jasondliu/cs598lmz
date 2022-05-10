import socket
socket.if_indextoname(3)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.7/socket.py", line 225, in if_indextoname
    return _socket.if_indextoname(interface)
socket.error: (99, 'Cannot assign requested address')
</code>
I have tried to use the following command to get the interface name:
<code>ip addr show | grep -w inet | awk '{print $NF}' | sed -e 's/://'
</code>
But it gives the following output:
<code>lo
</code>
I have also tried to use the following command:
<code>ip addr show | grep -w inet | awk '{print $2}'
</code>
But it gives the following output:
<code>127.0.0.1/8
</code>
I have also tried to use the following command:
<
