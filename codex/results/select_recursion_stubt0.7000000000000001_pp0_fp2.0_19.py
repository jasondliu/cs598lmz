import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass

def test_parse_select_errors():
    # select.select should raise ValueError if the list arguments
    # contain the same object more than once.
    a = []
    class F:
        def fileno(self):
            return a.pop()
    f = F()
    a.append(f)
    try:
        select.select([f, f], [f, f], [f, f])
    except ValueError:
        pass

def test_poll_errors():
    # select.poll should raise ValueError if the list arguments
    # contain the same object more than once.
    p = select.poll()
    a = []
    class F:
        def fileno(self):
            return a.pop()
    f = F()
    a.append(f)
    p.register(f, select.POLLIN)
    try:
       
