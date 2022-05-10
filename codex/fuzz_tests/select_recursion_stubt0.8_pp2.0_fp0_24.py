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

    bar_code = bar.__code__
    bar_code = types.CodeType(bar_code.co_argcount, bar_code.co_kwonlyargcount, bar_code.co_nlocals, bar_code.co_stacksize, bar_code.co_flags, bar_code.co_code, bar_code.co_consts, bar_code.co_names, bar_code.co_varnames, bar_code.co_filename, bar_code.co_name, bar_code.co
