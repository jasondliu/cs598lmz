import select
# Test select.select()

def test_select():
    import select
    import socket

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(5)
    port = s.getsockname()[1]
    print 'listening on port', port
    r, w, e = select.select([s], [], [], 5)
    if s in r:
        print 'socket is readable'
    else:
        print 'socket is not readable'
    s.close()

if __name__ == '__main__':
    test_select()
