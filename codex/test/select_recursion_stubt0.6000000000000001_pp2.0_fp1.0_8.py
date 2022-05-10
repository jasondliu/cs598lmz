import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    f = F()
    a.append(f)
    select.select([], [], a)

def test_unhashable():
    def f():
        return {}
    class F:
        def fileno(self):
            return 0
    a = F()
    try:
        select.select([], [a], a, 0)
        assert False
    except TypeError:
        pass

def test_select_bad_fd():
    import subprocess
    import os
    p = subprocess.Popen([os.path.join(os.getcwd(), "badfd.py")],
                         stdout=subprocess.PIPE)
    try:
        p.wait()
        assert False
    except OSError:
        pass
    if p.stdout is not None:
        p.stdout.close()
    p.wait()

def test_select_bad_fd_select():
    import subprocess
    import os
