import socket
# Test socket.if_indextoname()
class socket_test:

    def __init__(self, ifname):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.ifname = ifname
        if(self.ifname == "em2"):
            self.ifname = 'enp0s25'
        self.ifname= self.ifname.encode('utf-8')

    def if_nametoindex(self):
        self.s.bind((self.ifname, 0))

    def if_indextoname(self):
        self.s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, self.ifname)

    def if_nametoiaddr(self):
        self.s.bind((socket.if_indextoname(self.s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE), 0, self.ifname)))

def test():
    tfindex = socket_test("eth0")

