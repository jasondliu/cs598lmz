import socket
socket.if_indextoname(i)

# get extended stats from the network interface
import struct
def get_sock_extended(s):
    buf=s.getsockopt(socket.SOL_SOCKET, SO_EE_ORIGIN_TIMESTAMPING, 12)
    ts = struct.unpack('IIII', buf)
    print "recv:", ts[0]

    buf=s.getsockopt(socket.SOL_SOCKET, SO_EE_OFFENDER, 12)
    ts = struct.unpack('IIII', buf)
    print "offending:", ts[0]

# via http://ubuntuforums.org/showthread.php?t=1832963
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
   
