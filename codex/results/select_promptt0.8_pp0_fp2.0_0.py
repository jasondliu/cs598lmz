import select
# Test select.select

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', port))
    s.listen(1)
    s.setblocking(0)
    while 1:
        try:
            clientsock, clientaddr = s.accept()
        except socket.error, e:
            import errno
            if e.args[0] != errno.EAGAIN:
                raise
            print "accept exception:", e.args
        else:
            print "connection from", clientsock.getpeername()
            clientsock.setblocking(0)
            clientsock.send('hello')

def testselect():

    port = 50007
    threading.Thread(target=server, args=(port,)).start()

    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(
