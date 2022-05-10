import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)
            return 0

    select.select([F()], [], [], 0)

def test_select_closed():
    class F:
        def fileno(self):
            return 0
    
    f = F()
    f.close = lambda: None
    select.select([f], [], [], 0)

def test_select_close_fd():
    class F:
        def fileno(self):
            return 0

    class F2:
        def close(self):
            f.close = lambda: None

    f = F()
    f2 = F2()
    f.close = lambda: f2.close()
    select.select([f], [], [], 0)

def test_select_bad_fd():
    class F:
        def fileno(self):
            return -1
    
    try:
        select.select([F()], [], [], 0)
    except ValueError:
        pass

run_test(__name__)
