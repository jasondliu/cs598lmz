import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    try:
        select.select([f], [], [])
    except IndexError:
        pass
    else:
        assert False

def test_select_readwrite():
    for i in range(2):
        r, w, x = select.select([], [], [], 0)
        assert r == []
        assert w == []
        assert x == []

def test_select_readwrite_timeout():
    import time, os
    r, w, x = select.select([], [], [], 1)
    assert r == []
    assert w == []
    assert x == []
    time.sleep(2)
    # this tests that the timeout is not a total timeout
    # XXX not sure how to test this, so just checking that we didn't
    #     hang
    r, w, x = select.select([], [], [], 1)
    assert r == []
    assert w == []
    assert x == []

def test_select_keyboardinterrupt():
    import os

