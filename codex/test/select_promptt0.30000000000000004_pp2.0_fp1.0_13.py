import select
# Test select.select()

def test_select():
    import os
    import select
    import socket
    import time

    # Create two sockets
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind them to two random ports
    s1.bind(('', 0))
    s2.bind(('', 0))

    # Get the ports
    port1 = s1.getsockname()[1]
    port2 = s2.getsockname()[1]

    # Start listening on both
    s1.listen(1)
    s2.listen(1)

    # Start a client and connect to s1
    pid = os.fork()
    if pid == 0:
        time.sleep(1)
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(('localhost', port1))
        os._exit(0)

    # Accept the connection
