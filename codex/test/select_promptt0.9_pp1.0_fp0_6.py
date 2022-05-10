import select
# Test select.select()
def listen():
    """
    Return a socket object, bound to the guest interface's virtual NIC and
    listening for inbound TCP connections.
    """
    # listen on guest NIC
    host = "10.10.10.1"
    port = 3000
    backlog = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # avoid socket already in use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))
    s.listen(backlog)
    return s

s = listen()
