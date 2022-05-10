import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(('localhost', port))
    s3, addr = s.accept()
    s2.send(b'x')
    for i in range(5):
        print(i)
        r, w, e = select.select([s3], [], [], 1.0)
        if s3 in r:
            print(s3.recv(1))
            break
        time.sleep(1)
    else:
        raise RuntimeError("timeout")
    s3.close()
    s2.close()
    s.close()

test_select()
