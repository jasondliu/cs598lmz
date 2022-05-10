import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(None)

    f = F()
    # we return an iterator, so this will exhaust the iterator,
    # and cpython's select.select will mutate the list.
    select.select([f], [], [])
    for _ in a:
        pass
    # we return a list, so this will return True
    assert select.select([], [], [f], 0) == ([], [], [])
    # this is where we go wrong in the regression test:
    # the object is still in the list, but it's been deleted
    # and replaced with a new object
    assert not a, a
    # this causes a segfault because the object is already
    # deallocated
    select.select([f], [], [])

def test_select_select_error():
    c = select.select([b'abc'], [], [])
    assert isinstance(c[0][0], bytes)
    assert c[0][0] == b'abc'
