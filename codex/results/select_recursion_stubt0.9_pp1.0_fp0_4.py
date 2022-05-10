import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 7
        def read(self, _):
            a.append(None)
            return 0
    
    select.select([F()], [], [], 0.0) == ([], [], [])
    assert a == [None]


def test_select_times():
    select.select([], [], [], 0.0) == ([], [], [])
    select.select([], [], [], 1.0) == ([], [], [])
