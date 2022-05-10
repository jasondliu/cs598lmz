import select


from server import Connection, ConnectionHandler, ConnectionPool


class TestConnection(Connection):
    """
    A connection that reads and writes to files rather than sockets.
    """
    def __init__(self, input_file=None, output_file=None):
        self.input_file = input_file or StringIO()
        self.output_file = output_file or StringIO()
        super(TestConnection, self).__init__(self.input_file, self.output_file)

    def close(self):
        self.input_file.close()
        self.output_file.close()


class TestHandler(ConnectionHandler):
    """
    A handler for TestConnection instances.
    """
    def handle(self, request):
        return 'Hello'


def test_connection_pool():
    """
    Test our connection pool with a bit of setup and teardown.
    """
    # Setup
    handler = TestHandler()
    pool = ConnectionPool(handler)

    # Test
    conn = TestConnection()
    pool.add_connection(conn)

