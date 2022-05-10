import select
# Test select.select
class TestSelect(unittest.TestCase):

    def test_select(self):
        server = socket.socket()
        server.bind(("127.0.0.1", 0)) # Bind to a free port provided by the host.
        server.listen(1) # Limit the queue of waiting connections.

        conn, addr = server.accept()
        self.assertEqual(select.select([conn],[],[],0), ([conn], [], []))

        conn.close()
        server.close()

    def test_select_timeout(self):
        server = socket.socket()
        server.bind(("127.0.0.1", 0)) # Bind to a free port provided by the host.
        server.listen(1) # Limit the queue of waiting connections.

        start = time.time()
        self.assertEqual(select.select([server],[],[],1), ([], [], []))
        self.assertTrue(time.time() - start >= 1, "Timed out too early")

        conn, addr = server.accept()
