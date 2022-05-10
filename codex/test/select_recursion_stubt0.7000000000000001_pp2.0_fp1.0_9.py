import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    f = F()
    select.select([f], [], [])
    select.select([f], [], [])
    assert len(a) == 1

def test_select_error():
    raises(ValueError, select.select, [], [], [], -1)

def test_select_keyboard_interrupt():
    with raises(KeyboardInterrupt):
        select.select([], [], [], 1)

def test_select_interrupt_error():
    with raises(IOError, match="interrupted system call"):
        select.select([], [], [], 1)
