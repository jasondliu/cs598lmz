import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
# Test ctypes.util.find_library
libc_name = ctypes.util.find_library('c')
libc = ctypes.CDLL(libc_name)
# Test threading.Thread
t = threading.Thread()
t.start()

# Test libnacl
import libnacl as nacl

class TestVectors(unittest.TestCase):
    def test_crypto_box(self):
        # test vectors from http://nacl.cr.yp.to/box.html
        alicepk = nacl.decode(b'77b7fa410c9ac58a25f49bc8e5083a2c4c7d1e4e700d87a5f7c0e938e8f88ff1')
        alicesk = nacl.decode(b'77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a')
