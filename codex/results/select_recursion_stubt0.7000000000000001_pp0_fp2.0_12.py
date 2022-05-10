import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    def f():
        select.select([F()], [], [], 0.1)

    a = [0]
    f()
    a.append(1)
    f()
    try:
        a.append(2)
        raises(AttributeError, f)
    finally:
        a.pop()
    a.append(3)
    raises(select.error, f)

def test_select_error():
    raises(OSError, select.select, [], [], [], 0.1)

def test_select_macosx_error():
    # issue #2253
    if sys.platform == 'darwin':
        raises(OSError, select.select, [], [], [], 0.1)

class MyFileObj:
    def __init__(self, content):
        self._content = content

    def fileno(self):
        return -1

    def read(self, size):
        return self._content

def test_select_epoll():
    import os
    if hasattr
