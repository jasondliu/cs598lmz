import socket
import struct
import time
import sys

# http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__ == '__main__':
    try:
        while True:
            print 'IP address: %s' % get_ip_address('eth0')
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
