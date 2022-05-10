import select
# Test select.select function

# output list
out = []


def write_chunck(sock):
    sock.send('hello world')
    out.append(sock)
    print 'send [hello world] through', sock.getpeername()


def read(sock):
    print sock.recv(1024)
    out.remove(sock)


lsock = socket.socket()
lsock.bind(('127.0.0.1', 9999))
lsock.listen(5)

while True:
    rl, wl, xl = select.select((lsock, ), (), (), 0.1)
    for r in rl:
        if r is lsock:
            ns, naddr = lsock.accept()
            write_chunck(ns)
            print 'accept', naddr

#        else:
#            read(r)
    if len(out) == 0:
        # continue
        print 'Continue'

    else:
        conns = out.copy()
        rl, wl, xl = select.
