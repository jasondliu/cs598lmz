import socket
socket.if_indextoname('3')

print "============================================================"

def get_ips(iface_name_list):
    iface_list = [get_net_iface(name) for name in iface_name_list]
    return [iface.get_ipv4_addr() for iface in iface_list if iface.get_ipv4_addr()]

def get_net_iface(iface_name):
    try:
        iface = NetworkInterface(iface_name)
    except ifaddr.errors.InterfaceNotFoundError as e:
        print_err("Error: cannot use interface '%s' for sniffing: %s" % (iface_name, e))
        sys.exit(1)
    return iface

def get_all_addresses(iface_name_list):
    iface_list = [get_net_iface(name) for name in iface_name_list]
    return [iface.get_all_addresses() for iface in iface_list]

netifaces.AF_INET
