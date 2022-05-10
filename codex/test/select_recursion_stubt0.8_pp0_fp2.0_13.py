import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()
    
    select.select([F()], [], [], 0)

def test_select_mutated_read():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

def test_select_mutated_write():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([], [F()], [], 0)

def test_select_mutated_error():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([], [], [F()], 0)

@pytest.mark.skipif(not hasattr(select, "poll"), reason="poll not supported")
def test_poll_mutated():
    a = []

