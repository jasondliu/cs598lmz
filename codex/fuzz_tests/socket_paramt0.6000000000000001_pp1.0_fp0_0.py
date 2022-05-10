import socket
socket.if_indextoname(3)
</code>
But how do I get the interface name from the IP address? e.g. how do I get <code>en0</code> from <code>192.168.1.10</code>, or <code>en1</code> from <code>192.168.2.10</code>?


A:

I don't know if there is a way to get the interface name from the IP address. However, you can get the IP address from the interface name:
<code>import socket
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
</code>
You can get the list of interfaces using:
<code>&gt;&gt;&gt; import netifaces
&gt;&
