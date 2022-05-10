import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(0)
            return 3

    x = select.select([F()], [], [])
    assert a == [0]

def test_select_mutated_2():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 3

    x = select.select([F()], [], [], 0.0)
    assert a == [0]

def test_select_mutated_3():
    a = []

    class F:
        def fileno(self):
            a.append(0)
            return 3

    x = select.select([F()], [], [], 0.0, 0.0)
    assert a == [0]

def test_select_float():
    import sys
    if sys.platform == 'win32':
        skip("not supported on windows")

    # select.select() used to accept only ints as timeout
    # check that it now accepts floats too
    select.select([], [], [], 0.1)
    select.select
