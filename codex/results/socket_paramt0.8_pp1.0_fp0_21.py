import socket
socket.if_indextoname(2)

# If you want to see the routing table, use
R = execute(["ip", "route", "show", "dev", "eth0"])
print R.stdout

#
# If you need to ping something, use:
#

print execute(["ping", "-c", "2", "google.com"]).stdout

#
# To get the IP address, use:
#

print execute(["ifconfig", "eth0", "|", "grep", "inet", "|", "awk", '"{print" $2 "}"'])
