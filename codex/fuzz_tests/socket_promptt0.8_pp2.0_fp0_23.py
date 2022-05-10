import socket
# Test socket.if_indextoname(7)

try:
    import ifaddr
except ModuleNotFoundError:
    raise Exception("ifaddr module not installed, please install it.")

ifaces = ifaddr.get_adapters()

for iface in ifaces:
    if iface.nice_name != 'lo':
        print("Testing if_indextoname() for iface " + str(iface.nice_name))
        try:
            socket.if_indextoname(iface.index)
        except ValueError:
            raise ValueError("if_indextoname() did not find index " + str(iface.index) + ".")
