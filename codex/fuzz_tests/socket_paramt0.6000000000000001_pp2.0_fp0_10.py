import socket
socket.if_indextoname('{d7bcf852-a2c5-11e5-9912-001e8c717e5b}')
</code>
But it returns the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
socket.error: [Errno 22] Invalid argument
</code>
My environment:

Windows 10
Python 3.5.0

Can anyone help me?


A:

<code>import netifaces

def get_ip(iface):
    if netifaces.AF_INET in netifaces.ifaddresses(iface):
        return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']

get_ip('{d7bcf852-a2c5-11e5-9912-001e8c717e5b}')
</code>

