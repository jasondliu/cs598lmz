import socket
socket.if_indextoname(2)
'''

class Interface:
    def __init__(self, ip, netmask):
        self.ip = ip
        self.netmask = netmask
        #self.serial = serial
        self.mac = self.getMac()
        self.ifname = self.getIfName()
        #self.ifindex = self.getIfIndex()
        self.netid = self.getNetId()
        self.hostid = self.getHostId()
        self.broadcast = self.getBroadcast()

    # Returns the MAC address of the interface.
    def getMac(self):
        if self.ip == 'lo':
            return(0)
        else:
            return(get_mac_addr(self.ip))

    # Returns the interface name
    def getIfName(self):
        return(socket.if_indextoname(self.getIfIndex()))

    # Returns the interface index
    def getIfIndex(self):
        return(socket.if_nametoindex(self.getIfName()))

    # Returns the net
