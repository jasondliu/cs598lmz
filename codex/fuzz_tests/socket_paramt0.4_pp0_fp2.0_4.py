import socket
socket.if_indextoname(3)

if __name__ == "__main__":
    # get the interface name
    iface = socket.if_indextoname(3)
    # get the interface MAC address
    mac = get_mac_address(iface)
    # get the interface IP address
    ip = get_ip_address(iface)
    # get the interface subnet mask
    mask = get_netmask(iface)
    # get the interface broadcast address
    broadcast = get_broadcast_address(iface)
    # get the interface network address
    network = get_network_address(iface)
    # get the interface MTU
    mtu = get_mtu(iface)

    print("Interface: %s" % iface)
    print("MAC: %s" % mac)
    print("IP: %s" % ip)
    print("Subnet Mask: %s" % mask)
    print("Broadcast: %s" % broadcast)
    print("Network: %s" % network)
    print("MTU: %s" % mtu)
