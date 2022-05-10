import socket
# Test socket.if_indextoname
def net_interfaces():
    """Return a dict containing information about the system's network
    interfaces."""
    interfaces = {}
    for interface in socket.if_nameindex():
        name = interface[1]
        idx = interface[0]
        try:
            ip_addr = socket.if_indextoname(idx)
        except ValueError:
            ip_addr = None
        interfaces[idx] = {'idx': idx, 'name': name, 'addr': ip_addr}
    return interfaces
print(net_interfaces())
