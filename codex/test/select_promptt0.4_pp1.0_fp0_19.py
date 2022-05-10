import select
# Test select.select()

def test_select():
    import time
    import sys
    for i in range(10):
        print(i)
        rd, wr, er = select.select([sys.stdin], [], [], 1)
        if rd:
            print('input:', sys.stdin.readline().rstrip())
        time.sleep(1)

# test_select()

# Test select.poll()

def test_poll():
    import time
    import sys
    import select
    poller = select.poll()
    poller.register(sys.stdin, select.POLLIN)
    while True:
        print('polling...')
        events = poller.poll(1)
        print('events:', events)
        if events:
            print('input:', sys.stdin.readline().rstrip())
        time.sleep(1)

# test_poll()

# Test select.epoll()

def test_epoll():
    import time
    import sys
    import select
