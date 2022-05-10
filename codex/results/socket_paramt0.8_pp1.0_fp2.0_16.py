import socket
socket.if_indextoname(10)
</code>
It gives me:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.7/socket.py", line 732, in if_indextoname
    name.value = ifconf.ifc_req[ix].ifr_name
OSError: [Errno 22] Invalid argument
</code>
UPD: Trying out this code:
<code>import socket
socket.gethostbyname("localhost")
</code>
Gives me the same error as with previous code.


A:

The stack trace shows that it happens in line 732 of <code>/usr/local/lib/python3.7/socket.py</code>.
It looks like the problem is that your system does not support the IOCTLO_IFREQ_SIZES command in this particular way, but it is not clear why this is the case.

