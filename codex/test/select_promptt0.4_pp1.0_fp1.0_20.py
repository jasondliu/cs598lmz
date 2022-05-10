import select
# Test select.select()

def test_select():
    # Test the select() function
    import select
    for i in range(10):
        print(i, select.select([], [], [], 0.1))
    print(select.select([], [], [], 0.0))

def test_poll():
    # Test the poll() function
    import select
    p = select.poll()
    p.register(sys.stdin, select.POLLIN)
    for i in range(10):
        print(i, p.poll(1000))
    print(p.poll(0))

def test_epoll():
    # Test the epoll() function
    import select
    p = select.epoll()
    p.register(sys.stdin, select.EPOLLIN)
    for i in range(10):
        print(i, p.poll(1000))
    print(p.poll(0))

def test_kqueue():
    # Test the kqueue() function
    import select
    p = select.kqueue()
