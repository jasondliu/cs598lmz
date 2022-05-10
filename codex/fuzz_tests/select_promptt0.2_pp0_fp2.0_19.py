import select
# Test select.select()

def test_select():
    import select
    import socket
    import time

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.connect(("127.0.0.1", port))
    s3, addr = s.accept()
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4.connect(("127.0.0.1", port))
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5.connect(("127.0.0.1", port))
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6.connect(("127.0.
