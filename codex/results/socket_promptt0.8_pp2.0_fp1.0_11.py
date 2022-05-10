import socket
# Test socket.if_indextoname() of subinterface
#
# IFNAME: name of a subinterface
# IFINDEX: its index in if_nameindex()
#
# Expected result: the index returned by if_indextoname() for IFNAME 
# is IFINDEX.

if len(sys.argv) != 3:
	print("Usage: %s <ifname> <ifindex>" % sys.argv[0])
	sys.exit(1)

ifname = sys.argv[1]
ifindex = int(sys.argv[2])

if ifname != socket.if_indextoname(ifindex):
	print("if_indextoname(%d) != %s" % (ifindex, ifname))
	sys.exit(1)

print("if_indextoname(%d) == %s" % (ifindex, ifname))
sys.exit(0)
