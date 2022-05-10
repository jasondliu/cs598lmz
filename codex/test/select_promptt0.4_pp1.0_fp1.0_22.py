import select
# Test select.select()

def test_select():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 0))
    s.listen(1)
    s.setblocking(0)
    conn, addr = s.accept()
    conn.setblocking(0)
