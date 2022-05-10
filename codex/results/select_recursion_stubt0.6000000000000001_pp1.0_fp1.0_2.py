import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f.fileno())
    select.select([f], [], [])

def test_select_keyboardinterrupt():
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    try:
        select.select([F()], [], [])
    except KeyboardInterrupt:
        pass
    else:
        print("Expected KeyboardInterrupt")

def test_select_large_fd():
    try:
        select.select([], [], [], 0, 0)
    except ValueError:
        pass
    else:
        print("Expected ValueError")

def test_select_large_timeout():
    try:
        select.select([], [], [], sys.maxsize, 0)
    except OverflowError:
        pass
    else:
        print("Expected OverflowError")

def test_select_large_timeout_float():
    try:
        select.select([], [], [], sys.maxsize, 1.5)

