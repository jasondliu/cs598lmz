import select
# Test select.select()
def test_select():
    a = ['hi', 'hello']
    print(select.select(a, a, a))

# Test select.poll()
def test_poll():
    p = select.poll()
    p.register(sys.stdin, select.POLLIN)
    while True:
        for (fd, event) in p.poll():
            if fd == sys.stdin.fileno():
                print(sys.stdin.readline())

# Test select.epoll()
def test_epoll():
    e = select.epoll()
    e.register(sys.stdin, select.EPOLLIN)
    while True:
        for (fd, event) in e.poll():
            if fd == sys.stdin.fileno():
                print(sys.stdin.readline())

# Test select.kqueue()
def test_kqueue():
    k = select.kqueue()
