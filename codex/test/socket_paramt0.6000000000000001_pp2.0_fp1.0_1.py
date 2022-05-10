import socket
socket.if_indextoname(0)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def get_ip_address_all():
    interfaces = ["eth0","wlan0","wlan1"]
    ips = []
    for ifaceName in interfaces:
        try:
            ip = get_ip_address(ifaceName)
            ips.append((ifaceName,ip))
        except IOError:
            pass
    return ips

def get_ip_address_eth0():
    return get_ip_address("eth0")

def get_ip_address_wlan0():
    return get_ip_address("wlan0")

