import socket
socket.if_indextoname(1)
</code>
Result is as expected: 'en0'
For Windows users:
<code>socket.if_indextoname(1)
</code>
Result: '\Device\NPF_{9BD5FE71-5B5B-44F2-A51B-C3F11E84F9DC}'
You can see the list of interfaces by running:
<code>wmic nic get name
</code>
If you see something like this in here, then you need to run the first method
<code>Local Area Connection
PPP Adapter
</code>

