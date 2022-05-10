import select
# Test select.select()

def run_select_test(sock_in, sock_out):
    """
    Tests that select() works properly with sockets.
    """
    # Send a message to the other end.
    sock_out.sendall(b'Hello, World!')

    # Wait for the message to be received.
    while True:
        r, w, x = select.select([sock_in], [], [])
        if not r:
            continue
        assert sock_in in r

        data = sock_in.recv(1024)
        if not data:
            break

        assert data == b'Hello, World!'

        # Send back the same message.
        sock_out.sendall(data)

        break

def test_select(devnull, tmpdir):
    """
    Tests that select() works properly with sockets.
    """
    sock_path = str(tmpdir / 'sock')
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(sock_path)
    sock
