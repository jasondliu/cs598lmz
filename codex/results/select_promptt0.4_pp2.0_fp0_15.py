import select
# Test select.select() for reading and writing

def poll_for_data(sock):
    """Poll the socket for data"""
    while True:
        # Wait for at least one of the sockets to be ready for processing
        print '\nwaiting for the next event'
        readable, writable, exceptional = select.select(sock, sock, sock)
        print '\nready sockets:', readable
        print '\nwritable sockets:', writable
        print '\nexceptional sockets:', exceptional
        for s in readable:
            print '\n  READABLE:', s.getpeername()
            data = s.recv(1024)
            if not data:
                print '  closing', s.getpeername()
                s.close()
            else:
                print '  received "%s" from %s' % (data, s.getpeername())
        for s in writable:
            print '\n  WRITABLE:', s.getpeername()
            s.send('this is a test')
        for s in exceptional:
            print '\n  EX
