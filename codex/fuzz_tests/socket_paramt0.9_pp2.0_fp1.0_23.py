import socket
socket.if_indextoname(socket.if_nametoindex(interface))

'''
Returns an array of MAC addresses on an interface.
'''
def getIfHwAddrs(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]

'''
Used to launch a command with root user privileges.
'''
def sudo():
    return Popen(["sudo"])
