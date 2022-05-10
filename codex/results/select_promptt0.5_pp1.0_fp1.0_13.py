import select
# Test select.select()

def test_select():
    import socket
    import select

    s = socket.socket()
    s.setblocking(0)
    s.bind(('', 0))
    s.listen(1)
    s.accept()
    select.select([s], [], [])

def test_select_large_list():
    import socket
    import select

    s = socket.socket()
    s.setblocking(0)
    s.bind(('', 0))
    s.listen(1)
    s.accept()
    select.select([s] * 100, [], [])

def test_select_timeout():
    import socket
    import select

    s = socket.socket()
    s.setblocking(0)
    s.bind(('', 0))
    s.listen(1)
    s.accept()
    select.select([s], [], [], 1)

def test_select_write():
    import socket
    import select

    s = socket.socket()
    s.setblocking(0)
   
