import select
# Test select.select()



def _test_select():
    import _socket
    s = _socket.socket(2,1)
    s.bind(('',0))
    s.listen(5)
    s.setblocking(0)
    r,w,e = select.select([s],[s],[s],0)
    print(r,w,e)
    print(s in r, s in w, s in e)
    s.accept()
    r,w,e = select.select([s],[s],[s],0)
    print(r,w,e)
    print(s in r, s in w, s in e)
    s.close()


def _test_select_timeout():
    import _socket
    s = _socket.socket(2,1)
    s.bind(('',0))
    s.listen(5)
    s.setblocking(0)
    r,w,e = select.select([s],[],[],1.5)
    print(r,w,e)
    print(s in r, s
