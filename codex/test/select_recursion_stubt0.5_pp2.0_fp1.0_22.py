import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
    f = F()
    a.append(f)
    a.append(f)
    select.select([f], [f], [f], 0)

def test_select_keyboard_interrupt():
    def raiser():
        raise KeyboardInterrupt
    select.select([], [], [], 0, raiser)

def test_select_keyboard_interrupt_2():
    def raiser():
        raise KeyboardInterrupt
    try:
        select.select([], [], [], 0, raiser)
    except KeyboardInterrupt:
        pass
    else:
        raise Exception("didn't raise")

# ____________________________________________________________

def test_os_read_keyboard_interrupt():
    def raiser():
        raise KeyboardInterrupt
    os.read(0, 1)

def test_os_read_keyboard_interrupt_2():
    def raiser():
        raise KeyboardInterrupt
    try:
        os.read(0, 1)
    except KeyboardInterrupt:
        pass
   
