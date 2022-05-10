import socket
socket.if_indextoname(2)

interfaces = netifaces.interfaces()


def get_ip_address(interface):
    # return the first ip address we find for this interface
    return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']


def get_netmask(interface):
    # return the first netmask we find for this interface
    return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['netmask']


def get_mac_address(interface):
    return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']


def get_interface_name(ip):
    for interface in interfaces:
        try:
            if ip == get_ip_address(interface):
                return interface
        except KeyError:
            pass
    return None


def get_interface_ip_addresses(interface):
    try:
        return netifaces.ifaddresses(interface)[netifaces.AF_INET]
    except KeyError:
        return
