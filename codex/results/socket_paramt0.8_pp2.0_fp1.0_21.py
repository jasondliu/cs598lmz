import socket
socket.if_indextoname(2)

if not os.path.exists('/sys/class/net/'+iface+'/address'):
    print "Interface not found. Exiting..."
    sys.exit(1)

DEBUG = False

class Base:
    def __init__(self, interface, source, destination, verbose):
        self.interface = interface
        self.destination = destination
        self.source = source
        self.verbose = verbose
        self.s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

class ARP(Base):

    def __init__(self, interface, source, destination, verbose):
        Base.__init__(self, interface, source, destination, verbose)
        self.s.bind((interface, socket.htons(0x0800)))

    def arp(self):
        if self.verbose:
            print "Broadcasting magic ARP packet..."
        source_mac_bytes = binascii.unhexlify(self.source
