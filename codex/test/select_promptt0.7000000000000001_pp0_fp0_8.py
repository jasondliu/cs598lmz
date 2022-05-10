import select
# Test select.select

def test_select():
    # This is a test for a method that is supposed to be
    # platform independent.  Therefore, we use only generic
    # names in this test.
    # On Windows, network I/O is possible only on sockets.
    # On Unix, we test regular files.
    if sys.platform == 'win32':
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 0))
        server_socket.listen(1)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_socket.getsockname())
        server_socket.setblocking(False)
        client_socket.setblocking(False)
        conn, addr = server_socket.accept()
        conn.setblocking(False)
    else:
        tmpdir = tempfile.mkdtemp(prefix="pythontest_")
