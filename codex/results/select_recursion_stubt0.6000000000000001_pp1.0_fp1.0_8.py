import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    class F2:
        def fileno(self):
            return 2

    a = [F(), F2()]
    test_select_mutated()
    select.select(a, a, a, 0)


class TestSelect(unittest.TestCase):

    def setUp(self):
        self.save_flag = sys.flags.ignore_environment
        sys.flags.ignore_environment = True
        # create a pair of connected sockets
        self.serv, self.cli = socket.socketpair()

    def tearDown(self):
        sys.flags.ignore_environment = self.save_flag
        self.serv.close()
        self.cli.close()

    def test_select(self):
        self.serv.setblocking(0)
        self.cli.setblocking(0)
        # test the edge cases
        for i in (0, 1, 2):
            r, w, x = select.select([], [], [], 0)
            self.assertEqual(r, [])
            self.assertEqual(
