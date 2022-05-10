import select
# Test select.select()
def test_select():
    ready, _, _ = select.select([sys.stdin], [], [], 2)
    if ready:
        print('select.select() ready')
    else:
        print('select.select() not ready')

# Test select.poll()
def test_poll():
    poller = select.poll()
    poller.register(sys.stdin, select.POLLIN)
    ready = poller.poll(2)
    if ready:
        print('select.poll() ready')
    else:
        print('select.poll() not ready')

# Test select.epoll()
def test_epoll():
    epoller = select.epoll()
    epoller.register(sys.stdin, select.EPOLLIN)
    ready = epoller.poll(2)
    if ready:
        print('select.epoll() ready')
    else:
        print('select.epoll() not ready')

# Test select.kqueue()
def test_kqueue():
    kqueue = select.kqueue
