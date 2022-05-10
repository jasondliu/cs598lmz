import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated() # This will mutate a
            return len(a)

    s = select.select([F()], [], [], 0)
    # This should not raise IndexError, although it is highly likely
    # that an IndexError will be raised in the above implementation
    # because the mutating of a violates the documented assumptions of
    # the select.select implementation.
    del a[:]
    test_support.gc_collect()

def test_select_dispatchers():
    # Check that select dispatchers don't leave zombie or detached threads
    # behind.
    try:
        threading.Timer(1, lambda: None).start()
    except ValueError:
        pass
    else:
        return
    for domain in socket.getaddrinfo('google.com', 80, 0, 0,
                                  socket.IPPROTO_TCP):
        try:
            f = socket.socket(domain[0], domain[1], domain[2])
            f.connect(('::1', 80))
            fd = f.fileno()
        except socket.error:
            continue

