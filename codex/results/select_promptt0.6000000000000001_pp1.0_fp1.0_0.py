import select
# Test select.select()

def test_select():
    '''
    测试 select 模块
    '''
    import socket
    import select

    s = socket.socket()
    s.bind(('localhost', 9090))
    s.listen(100)

    rlist = [s]
    wlist = []
    xlist = []

    while True:
        rl, wl, xl = select.select(rlist, wlist, xlist, 1)
        for r in rl:
            if r is s:
                conn, addr = s.accept()
                rlist.append(conn)
            else:
                data = r.recv(1024)
                if not data:
                    rlist.remove(r)
                else:
                    print(data)
