import select
# Test select.select()

# Create a pair of connected sockets

if len(sys.argv) != 2:
    print >>sys.stderr, 'usage: %s <port>' % sys.argv[0]
    sys.exit(2)

port = int(sys.argv[1])

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Avoid bind() exception: OSError: [Errno 48] Address already in use
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind(('', port))
lsock.listen()
print 'listening on port', port

# Connect the sockets to each other, and shutdown one side

sock1, sock2 = socket.socketpair()
sock1.shutdown(socket.SHUT_WR)
sock2.shutdown(socket.SHUT_RD)

# Set up the poller

poller = select.poll()
pollmask = select.POLLIN
