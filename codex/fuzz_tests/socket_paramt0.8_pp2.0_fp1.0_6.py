import socket
socket.if_indextoname(i))
</code>
I've also tried:
<code>ip = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM),
                           0x8915,  # SIOCGIFADDR
                           struct.pack('256s', str(num).encode('utf-8'))))
</code>
and some other hacks but the result is always the same:
<code>Traceback (most recent call last):
  File "get-ip.py", line 10, in &lt;module&gt;
    print((socket.if_indextoname(i))
OSError: [Errno 19] No such device
</code>
I know that <code>tap0</code> is available as when I try <code>tcpdump -i tap0</code> I can see it getting traffic, otherwise I would not even attempt to run the script.
I've tried with Python 3.5.2 and 2.7.12
The solution works perfectly on other machines (same distro - Debian 8).
