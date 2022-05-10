import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return fd

        def read(self, n):
            pass

    a.append(F())

    fd = 3
    try:
        select.select(a, [], [])
    except IndexError:
        pass


import select
import sys
if sys.platform[:3] == 'win':
    pass
elif sys.platform == 'darwin':
    # XXX: Hack: try to not block on darwin for now
    fd = open('/dev/null', 'r')
    class F:
        def fileno(self):
            return fd

        def read(self, n):
            pass

    a = []
    a.append(F())
    select.select(a, [], [], 0)
    fd.close()

def test_select_2wparam():
    import select
    sel = select.select([], [], [], 0.9)

def test_select_wparam():
    import select
    sel = select.select([], [], [])

def test_select_4
