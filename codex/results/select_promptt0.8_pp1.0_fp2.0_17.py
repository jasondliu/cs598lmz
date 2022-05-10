import select
# Test select.select()

def poll():
    # Create a pair of connected sockets
    if os.name == 'nt':
        import socket
        readsock, writesock = socket.socketpair()
    else:
        # On Unix, create a pair of connected file descriptors
        # On Linux, use SOCK_NONBLOCK as a flag to socketpair() to avoid blocking
        # on connect().
        read_fd, write_fd = os.socketpair(socket.AF_UNIX, socket.SOCK_STREAM | socket.SOCK_NONBLOCK)

        # Turn the file descriptors into sockets
        readsock = socket.fromfd(read_fd, socket.AF_UNIX, socket.SOCK_STREAM)
        writesock = socket.fromfd(write_fd, socket.AF_UNIX, socket.SOCK_STREAM)

    # Set the sockets to be non-blocking
    readsock.setblocking(0)
    # writesock.setblocking(0)

    # Create a new poll object
    poller = select.poll()
    
    # Register the sockets
