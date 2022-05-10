import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)
        def read(self):
            return 'abc'

    def g():
        f = F()
        a.append(f)
        select.select([f], [], [])

    raises(RuntimeError, g)


def test_connect_mutated():
    try:
        select.select([], [], [], .001)
    except select.error:
        pass

    a = []

    class F:
        def fileno(self):
            test_connect_mutated()
            return len(a)
        def read(self):
            return 'abc'

    def g():
        f = F()
        a.append(f)
        select.select([], [f], [], .001)

    raises(RuntimeError, g)

def test_accept_mutated():
    try:
        select.select([], [], [], .001)
    except select.error:
        pass

    a = []

    class F:
        def fileno(self):
            test_accept_mutated()
           
