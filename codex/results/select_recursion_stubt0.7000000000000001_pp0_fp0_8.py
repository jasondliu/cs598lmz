import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(self)
            return 1

    f = F()
    select.select([f], [f], [f])
    assert a

def test_select_large_fds():
    a = []
    class F:
        def fileno(self):
            a.append(self)
            return len(a) + 3

    f1, f2, f3 = F(), F(), F()
    select.select([f1, f2, f3], [f1, f2, f3], [f1, f2, f3])
    assert a == [f1, f2, f3]

def test_select_negative_fds():
    # regression test for issue #746
    import subprocess

    p = subprocess.Popen([sys.executable, '-c',
        "import sys; sys.stdout.write('x')"],
        stdout=subprocess.PIPE)
    for i in range(3):
        select.select([p.stdout], [], [])
        p.stdout.
