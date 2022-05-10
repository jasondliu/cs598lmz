import socket
socket.if_indextoname(2)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print get_ip_address('eth0')

# http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
# http://stackoverflow.com/questions/24196932/how-can-i-get-the-ip-address-of-eth0-in-python
# https://gist.github.com/phatblat/1713458
# https://gist.github.com/phatblat/1713458
# http://stackoverflow.com/questions/166506/finding-local-ip-addresses-
