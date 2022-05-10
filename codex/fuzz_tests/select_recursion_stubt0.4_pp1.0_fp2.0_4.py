import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    f = F()
    a.append(f)
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass
    a.remove(f)
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass
    a.append(f)
    try:
        select.select([], [], [], 0)
    except ValueError:
        pass

def test_select_keyboardinterrupt():
    class F:
        def fileno(self):
            raise KeyboardInterrupt
    f = F()
    try:
        select.select([f], [], [], 0)
    except KeyboardInterrupt:
        pass

def test_select_error():
    class F:
        def fileno(self):
            raise OSError
    f = F()
    try:
        select.select([f], [], [], 0)
    except OSError:
        pass

def test_select_bad_fd():
   
