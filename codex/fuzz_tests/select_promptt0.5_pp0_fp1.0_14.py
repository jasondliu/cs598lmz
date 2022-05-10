import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 80))
    print "sock:", sock
    print select.select([sock], [], [])
    time.sleep(1)
    print select.select([sock], [], [])
    sock.close()

def test_select_timeout():
    import select
    import socket
    import time
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 80))
    print "sock:", sock
    print select.select([sock], [], [], 1)
    time.sleep(1)
    print select.select([sock], [], [], 1)
    sock.close()

def test_select_timeout_2():
    import select
    import socket
    import time
    sock = socket.socket(socket.AF_INET, socket.
