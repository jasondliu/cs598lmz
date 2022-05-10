import select
# Test select.select()

def run():
    try:
        poller = select.epoll()
    except:
        poller = select.poll()
    #
    # Create two sockets
    #
    s1 = socket.socket()
    s2 = socket.socket()
    port1 = get_port()
    port2 = get_port()

    s1.bind(('localhost', port1))
    s2.bind(('localhost', port2))
    s1.listen(1)
    s2.listen(1)

    poller.register(s1, select.POLLIN)
    poller.register(s2, select.POLLIN)

    c1 = socket.socket()
    c2 = socket.socket()
    c1.connect(('localhost', port1))
    c2.connect(('localhost', port2))

    c1.sendall(b"hello")
    c2.sendall(b"world")

    # Allow the sockets to receive the data
    time.sleep(0.01)

    if poller.poll():
