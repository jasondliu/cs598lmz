import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()

    select.select([], [], [F()])
    a.append(a)

def test_weakref():
    import weakref, os, subprocess

    # On Windows, subprocess.Popen holds a weak reference to a
    # Popen3 object with a file descriptor, which in turn holds
    # a weak reference to its underlying file object, the latter
    # being able to create a reference cycle.  The following
    # should not leak memory.
    for i in xrange(100):
        p = subprocess.Popen([os.path.dirname(sys.executable)])
        wr = weakref.ref(p.stdin)
        p.stdin.close()
        if None in (wr(), p.stdin):
            break

def test_os_getcwd_corner_case():
    import os
    known_size = len(os.getcwd())
    while True:
        try:
            r = os.read(0, known_size * 2)
            assert False, "no blocking on read() anymore!?"
        except
