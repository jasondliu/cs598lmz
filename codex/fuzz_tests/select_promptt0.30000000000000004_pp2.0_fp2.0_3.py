import select
# Test select.select

def test_select():
    import select
    for i in range(10):
        print(select.select([], [], [], 0.1))

# test_select()

# Test select.poll

def test_poll():
    import select
    p = select.poll()
    p.register(1, select.POLLIN)
    print(p.poll(1))

# test_poll()

# Test select.epoll

def test_epoll():
    import select
    p = select.epoll()
    p.register(1, select.EPOLLIN)
    print(p.poll(1))

# test_epoll()

# Test select.kqueue

def test_kqueue():
    import select
    p = select.kqueue()
    p.control([select.kevent(1, select.KQ_FILTER_READ, select.KQ_EV_ADD)], 0)
    print(p.control([], 1))

# test_kqueue()

# Test select.devpoll

