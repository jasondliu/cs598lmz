import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 'en0' + chr(0))
print(s.getsockname())
</code>
Output:
<code>(2, 1)
</code>
As you can see, the output is a tuple of two integers.  The second integer is the interface index, which you can also get with <code>socket.if_nametoindex()</code>.

