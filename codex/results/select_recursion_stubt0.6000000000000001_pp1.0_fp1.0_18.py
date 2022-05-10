import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1

    a.append(F())
    try:
        select.select([], [], [])
    except ValueError:
        pass
    else:
        assert False, "ValueError was not raised"

def test_select_keyboard_interrupt():
    a = []

    class F:
        def fileno(self):
            return 1

        def read(self, count):
            raise KeyboardInterrupt

    a.append(F())
    try:
        select.select([], [], [])
    except KeyboardInterrupt:
        pass
    else:
        assert False, "KeyboardInterrupt was not raised"

def test_select_error():
    a = []

    class F:
        def fileno(self):
            return 1

        def read(self, count):
            raise OSError

    a.append(F())
    try:
        select.select([], [], [])
    except OSError:
        pass
    else:
        assert False, "OSError was not raised"

class TestSelect
