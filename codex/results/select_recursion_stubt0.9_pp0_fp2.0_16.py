import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    with pytest.raises(RuntimeError):
        select.select([F()], [], [], 1)
    a.append(1)
    assert a[:] == [1, 1]

def test_select_keyboard_interrupt():
    # See: https://bitbucket.org/pypy/pypy/issues/1737/selectignores-keyboardinterrupt
    #
    w = []
    def waiter():
        w.append('a')
        return select.select([], [], [], 1)

    t = Thread(target=waiter)
    t.daemon = True
    t.start()

    sleep(0.01)
    t.join()

    assert w == ['a']
