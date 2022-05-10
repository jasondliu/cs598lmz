import socket
socket.if_indextoname(int(input("Enter interface: ")))

def get_interface():
    interfaces = get_network_interfaces()
    for i in interfaces:
        print(i, interfaces[i])
    if len(interfaces) == 1:
        return list(interfaces)[0]
    else:
        return input("Which interface: ")

def get_network_interfaces():
    interfaces = {}
    for i in netifaces.interfaces():
        addrs = netifaces.ifaddresses(i)
        if netifaces.AF_INET in addrs:
            interface_data = addrs[netifaces.AF_INET][0]
            interfaces[i] = interface_data
    return interfaces

def get_ip(interface):
    interfaces = get_network_interfaces()
    return interfaces[interface]["addr"]

def get_mac(interface):
    interfaces = get_network_interfaces()
    return interfaces[interface]["peer"]

def get_netmask(interface):
    interfaces = get_network_interfaces()
    return interfaces
