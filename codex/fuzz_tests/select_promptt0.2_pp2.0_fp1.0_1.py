import select
# Test select.select()

def test_select():
    import select
    import socket
    import time
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    conn, addr = s.accept()
    print 'accepted', conn, addr
    conn.send('hello')
    print 'sent hello'
    time.sleep(1)
    print 'sleep done'
    r, w, e = select.select([conn], [], [], 1)
    print 'select done'
    if r:
        print 'r', r
        data = conn.recv(100)
        print 'received', `data`
    else:
        print 'no data'

if __name__ == '__main__':
    test_select()
