import socket
socket.if_indextoname(3)

# Output: 'Wi-Fi'
</code>
To get the IP address of the interface, you can use <code>socket.if_nameindex()</code> to get a list of the interfaces, and then <code>socket.if_nameindex()</code> again to get the IP address of the interface.

