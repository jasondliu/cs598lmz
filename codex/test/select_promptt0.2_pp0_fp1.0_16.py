import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    port = s.getsockname()[1]
    print('listening on port', port)
    r, w, x = select.select([s], [], [], 1.0)
    if s in r:
        conn, addr = s.accept()
        print('client connected')
        data = conn.recv(1024)
        print('received', data)
        conn.send(data)
        conn.close()
        s.close()
    else:
        print('timed out')

if __name__ == '__main__':
    test_select()
