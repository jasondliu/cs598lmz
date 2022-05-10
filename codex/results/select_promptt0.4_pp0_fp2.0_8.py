import select
# Test select.select()

def test_select():
    """
    >>> test_select()
    [], [], []
    [], [], []
    [], [], []
    """
    print select.select([], [], [], 0.0)
    print select.select([], [], [], 0.0)
    print select.select([], [], [], 0.0)

# Test select.poll()

def test_poll():
    """
    >>> test_poll()
    []
    []
    []
    """
    p = select.poll()
    print p.poll(0)
    print p.poll(0)
    print p.poll(0)

# Test select.epoll()

def test_epoll():
    """
    >>> test_epoll()
    []
    []
    []
    """
    p = select.epoll()
    print p.poll(0)
    print p.poll(0)
    print p.poll(0)

# Test select.kqueue()

def test_kqueue():
