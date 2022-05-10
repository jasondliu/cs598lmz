import select
# Test select.select()

def test_select_select(benchmark):
    def select_select():
        r, w, x = select.select([], [], [], 0.1)
    benchmark(select_select)

# Test select.poll()

def test_select_poll(benchmark):
    def select_poll():
        p = select.poll()
        p.poll(0.1)
    benchmark(select_poll)

# Test select.epoll()

def test_select_epoll(benchmark):
    def select_epoll():
        p = select.epoll()
        p.poll(0.1)
    benchmark(select_epoll)
