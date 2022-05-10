import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return fd

    select.select([F()], [], [])

def test_recursion():
    import os

    a = []

    def f(b):
        if len(b) >= 70:
            return
        try:
            f(b + 'x')
        except EOFError:
            a.append(b)

    def g():
        f('y')

    # Select in child
    pid = os.fork()
    if pid == 0:
        g()
        _exit(0)
    else:
        os.waitpid(pid, 0)

    # Poll in child
    pid = os.fork()
    if pid == 0:
        select.poll()
        g()
        _exit(0)
    else:
        os.waitpid(pid, 0)

    assert len(a) >= 2


def test_non_int():
    try:
        import msvcrt
        msvcrt.get_osfhandle
    except (ImportError, AttributeError):
        skip("Needs Windows")

