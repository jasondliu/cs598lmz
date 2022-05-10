import select
# Test select.select

def read_socks(rlist, wlist, xlist, timeout=0):
    if timeout is not None:
        from time import time as now
        # time module is needed to call now()
        end = now() + timeout
    while True:
        ready = select.select(rlist, wlist, xlist, timeout)
        if ready == ([], [], []):
            return
        if timeout is not None:
            timeout = end - now()
            if timeout < 0:
                return
        for sock in ready[0]:
            data = sock.recv(1024)
            if not data:
                sock.close()
                rlist.remove(sock)
            else:
                print('%s: got %r' % (sock.getpeername(), data))
        for sock in ready[1]:
            sock.send(b'This is a test\n')
        for sock in ready[2]:
            print('closing', sock.getpeername(), 'after exception')
            sock.close()
            rlist.remove(sock)

