import socket
# Test socket.if_indextoname()

# Base class for all socket tests
class SocketTester(unittest.TestCase):
    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 0))
        self.ipaddr = socket.inet_ntoa(fcntl.ioctl(
                self.sock.fileno(),
                SIOCGIFADDR,
                struct.pack('256s', self.ifname[:15])
                )[20:24])

    def tearDown(self):
        self.sock.close()

# Subclass for tests on the loopback interface
class LoopbackTester(SocketTester):
    def setUp(self):
        self.ifname = 'lo'
        SocketTester.setUp(self)

class LoopbackNameTest(LoopbackTester):
    def runTest(self):
        self.failUnlessEqual(socket.if_indextoname(1), self.ifname)

class Loop
