import select
# Test select.select

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
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s4.connect(('localhost', port))
    s5 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s5.connect(('localhost', port))
    s6 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s6.connect(('localhost', port))
    s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

