import socket
socket.if_indextoname(3)
</code>
I get the following error:
<code>AttributeError: 'module' object has no attribute 'if_indextoname'
</code>
I'm using Python 2.7.9.
Do you know how I can solve this?


A:

You need to use the <code>fcntl</code> module to do this:
<code>import fcntl, socket, struct

def get_interface_ip(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
</code>

