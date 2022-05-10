import select
# Test select.select()

def test_select():
    import select
    print(select.select([], [], [], 1))
    print(select.select([], [], [], 0))
    print(select.select([], [], [], -1))

# test_select()

# Test select.poll()

def test_poll():
    import select
    poll = select.poll()
    poll.poll()

# test_poll()

# Test select.epoll()

def test_epoll():
    import select
    epoll = select.epoll()
    epoll.poll()

# test_epoll()

# Test select.kqueue()

def test_kqueue():
    import select
    kqueue = select.kqueue()
    kqueue.control([], 0, 0)

# test_kqueue()

# Test select.devpoll()

def test_devpoll():
    import select
    devpoll = select.devpoll()
    devpoll.poll()

# test_devpoll()

# Test select.select
