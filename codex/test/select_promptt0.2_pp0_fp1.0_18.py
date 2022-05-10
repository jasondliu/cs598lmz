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
    s4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in range(5):
        print(i)
        r, w, e = select.select([s2], [], [], 1)
        if s2 in r:
            print('s2 is ready for reading')
        r, w, e = select.select([s3], [], [], 1)
        if s3 in r:
            print('s3 is ready for reading')
