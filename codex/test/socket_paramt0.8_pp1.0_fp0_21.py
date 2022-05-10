import socket
socket.if_indextoname(2)

# If you want to see the routing table, use
R = execute(["ip", "route", "show", "dev", "eth0"])
