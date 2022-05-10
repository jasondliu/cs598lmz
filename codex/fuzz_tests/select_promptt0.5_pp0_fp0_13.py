import select
# Test select.select()

def test_select():
    import _socket
    import time
    for timeout in [0.1, 0.2, 0.3, 0.4, 0.5]:
        print("timeout =", timeout)
        r, w, x = select.select([], [], [], timeout)
        print("r =", r)
        print("w =", w)
        print("x =", x)
        time.sleep(0.5)
    sock = _socket.socket()
    for timeout in [0.1, 0.2, 0.3, 0.4, 0.5]:
        print("timeout =", timeout)
        r, w, x = select.select([sock], [], [], timeout)
        print("r =", r)
        print("w =", w)
        print("x =", x)
        time.sleep(0.5)
    for timeout in [0.1, 0.2, 0.3, 0.4, 0.5]:
        print("timeout =", timeout)
        r, w, x = select.
