import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(5)
    s.setblocking(0)
    port = s.getsockname()[1]
    print 'listening on port', port
    readable, writable, exceptional = select.select([s], [], [], 5)
    print readable, writable, exceptional
    time.sleep(10)
    print 'done'

if __name__ == '__main__':
    test_select()
