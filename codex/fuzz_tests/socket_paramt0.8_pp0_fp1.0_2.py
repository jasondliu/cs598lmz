import socket
socket.if_indextoname(5)

def get_iface_macs():
    ifaces = netifaces.interfaces()
    dict = {}
    for iface in ifaces:
        iface_mac = netifaces.ifaddresses(iface)[netifaces.AF_LINK][0]['addr']
        iface_ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
        dict[iface] = {'ip': iface_ip, 'mac': iface_mac}
    return dict
