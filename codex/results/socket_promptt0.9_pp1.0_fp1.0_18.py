import socket
# Test socket.if_indextoname
# via: socketserver.test.test_socketserver.test_daemon_threads
class TestIfIndexToName(unittest.TestCase):    
    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_if_indextoname(self):
        self.assertIsInstance(socket.if_indextoname(1),str)
        self.assertRaises(OSError,socket.if_indextoname,1024)

if __name__ == "__main__":
    unittest.main()
