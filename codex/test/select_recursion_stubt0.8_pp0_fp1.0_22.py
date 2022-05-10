import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 1
        def readline(self):
            a.append(1)
            return '\n'

    f = F()
    select.select([f], [], [])
    raise Exception('Failed to catch select mutating fds.')
