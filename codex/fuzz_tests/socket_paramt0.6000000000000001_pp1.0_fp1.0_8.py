import socket
socket.if_indextoname('3')

#Output
'eth0'
</code>
It is also possible to get the interface name from the IP address:
<code>#!/usr/bin/env python
import socket
socket.if_nameindex()

#Output
[(1, 'lo'), (2, 'eth0'), (3, 'eth1')]
</code>

