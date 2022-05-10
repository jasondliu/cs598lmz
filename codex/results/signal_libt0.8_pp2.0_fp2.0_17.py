import signal
signal.signal(signal.SIGINT, lambda *_: sys.exit(-1))
# end of kludge

import subprocess
import socket
from common import *

class TestDict(TestCase):
    def setUp(self):
        self.pid = subprocess.Popen(["../dictd", "-v", "-p", "9999", "-D", "-d"]).pid

    def tearDown(self):
        os.kill(self.pid, signal.SIGKILL)

    def test_dict_dictionary(self):
        c = dict_client()
        c.connect()

        c.sendall("DEFINE wn vermin\r\n")
        c.recvuntil("150")
        c.recvline()
        c.recvline()
        c.recvline()

        c.sendall("DEFINE dict dict\r\n")
        c.recvuntil("150")
        c.recvline()
        c.recvline()
        c.recvline()

        c.sendall("SHOW
