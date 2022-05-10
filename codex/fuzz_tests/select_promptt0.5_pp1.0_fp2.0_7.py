import select
# Test select.select

def test_select():
    read, write, err = select.select([sys.stdin], [], [], 10)
    if read:
        print read
        print read[0].readline()
    else:
        print 'timeout'

# Test select.poll

def test_poll():
    p = select.poll()
    p.register(sys.stdin, select.POLLIN)
    events = p.poll(10)
    if events:
        print events
        print events[0][1]
        print sys.stdin.readline()
    else:
        print 'timeout'

# Test select.epoll

def test_epoll():
    e = select.epoll()
    e.register(sys.stdin, select.EPOLLIN)
    events = e.poll(10)
    if events:
        print events
        print events[0][1]
        print sys.stdin.readline()
    else:
        print 'timeout'

# Test select.kqueue

def test_kqueue():
