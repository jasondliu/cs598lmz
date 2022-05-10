import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 10

    try:
        a.append(F())
        select.select([], [], a, 0)
    except RuntimeError as e:
        assert str(e) == "I/O operation on closed file"
    else:
        assert False, "Did not raise RuntimeError"

def test_select_closed():
    a = []

    class F:
        def fileno(self):
            return 10

    try:
        a.append(F())
        select.select([], [], a, 0)
    except RuntimeError as e:
        assert str(e) == "I/O operation on closed file"
    else:
        assert False, "Did not raise RuntimeError"

def test_select_closed_str():
    a = []

    class F:
        def __str__(self):
            return "hello"

    try:
        a.append(F())
        select.select([], [], a, 0)
    except RuntimeError as e:
        assert str(e) == "I/O operation on closed file"
   
