import select
# Test select.select()

# Create a pair of connected sockets
if os.fork() == 0:
    print 'Child: Connecting...'
    time.sleep(5)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 16000))
    print 'Child: Connected!'
    sys.exit(0)

print 'Parent: Waiting for connection...'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 16000))
server.listen(1)

readable, writable, exceptional = select.select([server], [], [])

print 'Parent: Connected!'
server.close()
