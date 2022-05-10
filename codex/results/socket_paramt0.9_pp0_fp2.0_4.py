import socket
socket.if_indextoname('31')
</code>
It was using the Windows 'Local Area Connection 2' adapter which had been removed.
So, the simple solution is to use <code>pcapy.findalldevs()</code>

