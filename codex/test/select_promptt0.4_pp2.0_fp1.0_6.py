import select
# Test select.select()

# Create a pair of connected sockets
if sys.platform == 'win32':
    def socketpair(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0):
        # We create a connected TCP socket. Note the trick with setblocking(0)
        # that prevents us from having to create a thread.
        lsock = socket.socket(family, type, proto)
        lsock.bind(('localhost', 0))
        lsock.listen(1)
        addr, port = lsock.getsockname()
        csock = socket.socket(family, type, proto)
        csock.setblocking(False)
        try:
            csock.connect((addr, port))
        except socket.error as e:
            if e.args[0] != errno.WSAEWOULDBLOCK:
                raise
        csock.setblocking(True)
        ssock, _ = lsock.accept()
        lsock.close()
        return (ssock, csock)
else:
    socketpair = socket.socketpair
