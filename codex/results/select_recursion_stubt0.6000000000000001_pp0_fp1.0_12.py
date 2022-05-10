import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 1

    select.select([F()], [], [], 0)

def test_select_keyboard_interrupt():
    def fileno():
        raise KeyboardInterrupt
    select.select([fileno()], [], [], 0)

def test_select_keyboard_interrupt2():
    def fileno():
        raise KeyboardInterrupt
    select.select([], [fileno()], [], 0)

def test_select_keyboard_interrupt3():
    def fileno():
        raise KeyboardInterrupt
    select.select([], [], [fileno()], 0)

def test_select_keyboard_interrupt4():
    def fileno():
        raise KeyboardInterrupt
    select.select([fileno()], [fileno()], [fileno()], 0)

def test_select_keyboard_interrupt5():
    def fileno():
        raise KeyboardInterrupt
    select.select([fileno()], [fileno()], [fileno()], 0.0)
