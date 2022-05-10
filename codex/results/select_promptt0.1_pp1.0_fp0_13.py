import select
# Test select.select()

def test_select():
    import socket
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
    s6, addr = s.accept()
    s7 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s7.connect(('localhost', port))
    s8, addr = s.accept()
    s9 = socket.socket(socket
