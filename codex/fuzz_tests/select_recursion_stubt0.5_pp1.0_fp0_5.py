import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    f.fileno()
    select.select([f], [], [])

def test_select_closed_fd():
    a = []

    class F:
        def fileno(self):
            return a.pop()

    f = F()
    f.fileno()
    select.select([f], [], [])

def test_select_closed_pipe():
    r, w = os.pipe()
    os.close(r)
    select.select([], [w], [])

class MyFile:
    def fileno(self):
        return 42

def test_select_bad_file():
    f = MyFile()
    select.select([f], [f], [f])

def test_select_bad_fd():
    select.select([100], [100], [100])

def test_select_bad_list():
    select.select([None], [None], [None])
    select.select([None, None], [None, None], [None, None])

