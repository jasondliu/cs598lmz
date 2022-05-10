import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    import sys
    import os

    # Create two sockets
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind them to something
    s1.bind(('localhost', 0))
    s2.bind(('localhost', 0))

    # Get the port numbers
    port1 = s1.getsockname()[1]
    port2 = s2.getsockname()[1]

    # Create a server and a client
    pid = os.fork()
    if pid == 0:
        # Child
        s1.listen(1)
        conn, addr = s1.accept()
        time.sleep(1)
        conn.send(b'xxx')
        sys.exit(0)
    else:
        # Parent
        s2.connect(('localhost', port1))
