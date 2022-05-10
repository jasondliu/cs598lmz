import socket
# Test socket.if_indextoname()

print "Test socket.if_indextoname()"

print "All interfaces:"
print socket.if_indextoname(0)

print "Loopback:"
print socket.if_indextoname(1)

print "Ethernet:"
print socket.if_indextoname(2)

print "Wifi:"
print socket.if_indextoname(3)

print "Ppp:"
print socket.if_indextoname(4)

print "Pppoe:"
print socket.if_indextoname(5)

print "Vlan:"
print socket.if_indextoname(6)

print "Bond:"
print socket.if_indextoname(7)

print "Tun:"
print socket.if_indextoname(8)

print "Tap:"
print socket.if_indextoname(9)

print "Bridge:"
print socket.if_indextoname(10)

print "Vxlan:"
print socket.if_indextoname(
