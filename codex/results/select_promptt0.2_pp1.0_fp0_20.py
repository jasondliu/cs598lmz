import select
# Test select.select()

def test_select():
    import select
    for i in range(10):
        print(select.select([], [], [], 0.1))

# test_select()

# Test select.poll()

def test_poll():
    import select
    p = select.poll()
    p.register(sys.stdin)
    while True:
        print(p.poll(1000))

# test_poll()

# Test select.epoll()

def test_epoll():
    import select
    e = select.epoll()
    e.register(sys.stdin.fileno(), select.EPOLLIN)
    while True:
        print(e.poll(1000))

# test_epoll()

# Test select.kqueue()

def test_kqueue():
    import select
    k = select.kqueue()
    k.control([select.kevent(sys.stdin, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
    while True:
        print
