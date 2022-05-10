import select
# Test select.select on sockets.
import socket
import time


def debug(msg):
    sys.stderr.write(msg + '\n')


class SelectTest(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind(('', 0))
        self.port = self.listener.getsockname()[1]
        self.listener.listen(1)
        self.child_conn, self.parent_conn = socket.socketpair()
        self.pid = os.fork()
        if self.pid == 0:
            self.listener.close()
            self.child_conn.close()
            time.sleep(1)
            self._child()
            os._exit(7)
        self.parent_conn.close()

    def tearDown(
