import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    class G:
        def fileno(self):
            a.append(1)
            return 0

    select.select([F()], [G()], [], 0)
    assert not a

def test_select_keyboard_interrupt():
    def raise_keyboard_interrupt():
        raise KeyboardInterrupt

    class F:
        def fileno(self):
            return 0

    try:
        select.select([F()], [], [], 0, raise_keyboard_interrupt)
    except KeyboardInterrupt:
        pass
    else:
        assert False, "KeyboardInterrupt not raised"
