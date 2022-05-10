import socket
# Test socket.if_indextoname
intf = "lo"
index = socket.if_nametoindex(intf)
mn_platf.print_log("index for interface {} is {}".format(intf, index))
intf = socket.if_indextoname(index)
mn_platf.print_log("interface for index {} is {}".format(index, intf))
intf = "eth1"
index = socket.if_nametoindex(intf)
mn_platf.print_log("index for interface {} is {}".format(intf, index))
intf = socket.if_indextoname(index)
mn_platf.print_log("interface for index {} is {}".format(index, intf))
intf = "eth3"
index = socket.if_nametoindex(intf)
mn_platf.print_log("index for interface {} is {}".format(intf, index))
intf = socket.if_indextoname(index)
mn_platf.print_log("interface for index {} is {}".format(
