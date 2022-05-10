import select
# Test select.select()

def test_select():
    import select
    import socket
    import threading
    import time

    # Create two sockets and make them non-blocking
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for s in [s1, s2]:
        s.setblocking(0)

    # Connect the sockets to each other
    threading.Thread(target=lambda: s1.connect(('localhost', s2.getsockname()[1]))).start()
    s2.listen(1)
    conn, addr = s2.accept()

    # Make sure the connection is established before testing select()
    for i in range(5):
        r, w, e = select.select([s1], [], [], 0.1)
        if r:
            break
        time.sleep(0.1)

    # Test select()
    r, w, e = select.select([s1], [s
