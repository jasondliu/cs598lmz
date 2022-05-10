import select
# Test select.select()

# Create a pair of connected sockets

if os.name == 'posix':
    import socket
    socks = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(2)]
    for s in socks:
        s.bind(('', 0))
        s.listen(1)
    socks[0].connect(socks[1].getsockname())
    socks[1].accept()
else:
    import win32pipe, win32file
    socks = [win32pipe.CreateNamedPipe(r'\\.\pipe\pypipe%d' % i,
                                       win32pipe.PIPE_ACCESS_DUPLEX,
                                       win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
                                       1, 65536, 65536,
                                       300, None)
             for i in range(2)]
    win32pipe.ConnectNamedPipe(socks[0], None)

for s in socks:
    print
