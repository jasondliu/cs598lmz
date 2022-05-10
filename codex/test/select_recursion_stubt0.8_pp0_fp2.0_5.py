import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

    select.select([F()], a, a)

def test_select_closed_pipe():
    pipe = os.pipe()
    os.close(pipe[0])
    os.close(pipe[1])
    select.select([pipe[0]], [], [])

def test_select_closed():
    f = open(os.devnull)
    os.close(f.fileno())
    select.select([f], [], [])

def test_select_closed_again():
    f = open(os.devnull)
    f.close()
    select.select([f], [], [])

def test_select_attr_error():
    class F:
        def __getattr__(self, what):
            if what == 'fileno':
                raise AttributeError
            raise RuntimeError

    select.select([F()], [], [])

def test_select_value_error():
    class F:
        def fileno(self):
            return -1
