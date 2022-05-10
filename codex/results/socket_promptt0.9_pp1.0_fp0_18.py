import socket
# Test socket.if_indextoname
print socket.if_indextoname(0)

# Test socket.if_nameindex
print socket.if_nameindex()

# Test socket.if_nametoindex
print socket.if_nametoindex('lo')

# Test socket.if_up
##print socket.if_up('lo')

# socket.ip_address()

# socket.ip_prefix has not been implemented yet, skip it.

# Test socket.ip_route and struct iproute, routing table entry
print socket.ip_route()

# Test socket.ip_rule, get routing rule, not implemented yet
##print socket.ip_rule()

# Test socket.ipencap_add()
# Test socket.ipencap_del()
# Test socket.ipencap_delete()
# Test socket.ipencap_get()
# Test socket.ipencap_get_fd()
# Test socket.ipencap_list()
# Test socket.ipencap_show()

# Test socket.iproute_deladdr()
# Test socket.iproute_delfib
