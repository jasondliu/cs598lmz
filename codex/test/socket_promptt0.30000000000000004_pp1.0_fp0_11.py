import socket
# Test socket.if_indextoname()

def get_if_index(ifname):
    return socket.if_nametoindex(ifname)

def get_if_name(ifindex):
    return socket.if_indextoname(ifindex)

def get_if_names():
    return socket.if_nameindex()

def get_if_addresses(ifname):
    return socket.if_nameindex(ifname)

def get_if_mtu(ifname):
    return socket.if_mtu(ifname)

def get_if_flags(ifname):
    return socket.if_flags(ifname)

def get_if_hwaddr(ifname):
    return socket.if_hwaddr(ifname)

def get_if_addr(ifname):
    return socket.if_addr(ifname)

def get_if_netmask(ifname):
    return socket.if_netmask(ifname)

def get_if_broadaddr(ifname):
    return socket.if_broadaddr(ifname)

