import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    select.select([F()], [], [])
    assert len(a) == 1

def test_select_recursive():
    a = []

    class F:
        def fileno(self):
            return len(a)

    def callback():
        select.select([F()], [], [])
        assert len(a) == 1
        select.select([F()], [], [])
        assert len(a) == 2

    select.select([F()], [], [], callback=callback)
    assert len(a) == 1

def test_select_keyboard_interrupt():
    def callback():
        raise KeyboardInterrupt
    assert select.select([], [], [], callback=callback) == ([], [], [])

def test_select_error():
    def callback():
        raise ValueError
    py.test.raises(ValueError, select.select, [], [], [], callback=callback)

