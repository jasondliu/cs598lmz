import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()  # side effect!
            a.append(1)
            return 10
    f = F()

    list(select.select([f], [], [], 0.5))
    list(select.select([f], [], [], 0.5))


class TestSelect(unittest.TestCase):

    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, [], [], [], -1)
        self.assertRaises(ValueError, select.select, [], [], [], -2)

    def test_read(self):
        data = b"some data for you"
        r, w = socket.socketpair()
        w.setblocking(0)
        w.send(data)
        w.close()
        readable, w, x = select.select([r], [], [], 2)
        self.assertIn(r, readable)
        self.assertEqual(r.recv(1000), data)

    def test_write(self):
        r, w = socket.socketpair()

