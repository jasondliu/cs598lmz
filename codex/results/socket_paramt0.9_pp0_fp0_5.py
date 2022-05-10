import socket
socket.if_indextoname(1)
</code>
but getting TypeError: an integer is required


A:

<code>if_indextoname()</code> wants an interface index number, not a port number. (On Windows, the index is the <code>IF_NUMBER</code> from <code>GetAdaptersAddresses()</code>, on Linux/UNIX it's the <code>if_index</code> from <code>SIOCGIFINDEX</code>.)
If you're trying to get the interface associated with the socket, use <code>getsockname()</code> to get the network address of the socket and <code>if_nametoindex()</code> to translate that address to an interface index. (If the address isn't connected to any interface then <code>None</code> is returned.)
<code>#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 0))
print(socket.if_indextoname(s
