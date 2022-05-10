import socket
import struct
import sys


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage: %s interface" % sys.argv[0]
        sys.exit(1)
    print get_ip_address(sys.argv[1])
