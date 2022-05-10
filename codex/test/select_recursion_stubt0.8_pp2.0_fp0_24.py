import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    s = select.select([F(), F()], [], [])

@known_bug
def test_select_exceptional():
    class F:
        def fileno(self):
            raise Exception

    select.select([F()], [], [])

def test_exception_in_select():
    def foo():
        select.select([], [], [], 0)

    def bar():
        foo()

    def baz():
        bar()

    def qux():
        baz()

