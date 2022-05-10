import select
# Test select.select()

print 'Waiting for connection...'
rlist, wlist, xlist = select.select([server], [], [])
if rlist:
    connection, address = server.accept()
    print '...connected from:', address
    connection.setblocking(0)
    rlist = [connection]
    wlist = []
    xlist = []

    while True:
        rlist, wlist, xlist = select.select(rlist, wlist, xlist)
        if rlist:
            data = rlist[0].recv(1024)
            if not data:
                break
            print 'Received:', data
            wlist.append(rlist[0])
        if wlist:
            wlist[0].send(data)
            wlist = []
        if xlist:
            raise RuntimeError('Polling failed')

connection.close()
