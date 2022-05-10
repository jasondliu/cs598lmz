import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            raise ValueError

    class G:
        def fileno(self):
            return a[0]

    s = select.select([F(), G()], [], [])
    assert len(s) == 2

def test_select_reused():
    s = select.select([], [], [])
    s = select.select([], [], [])
    assert len(s) == 3

def test_select_exit_stack():
    a = []
    s = select.select([], [], [])
    assert len(s) == 3
    b = a
    del a
    import gc; gc.collect(); gc.collect(); gc.collect()
    assert len(b) == 3

@impl_detail("test uses private selectors module", indent=0)
def test_select_fd_disappear():
    import os
    import selectors as selectormodule

    class MyException(Exception):
        pass

    class MySelector(selectormodule.BaseSelector):
        def __init__(self, fd):
           
