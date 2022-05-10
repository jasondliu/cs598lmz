import socket
# Test socket.if_indextoname
print(socket.if_indextoname(2))
# Should return the string of the network-interface name with index 2
print(socket.if_indextoname(3))
# Should return the string of the network-interface name with index 2
</code>
The code above should return <code>eth0</code> and <code>eth1</code> on RHEL 7.2 for example. What do you get?

