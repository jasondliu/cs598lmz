import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a[0]

        def readinto(self, dest):
            return test_select_mutated()
    class F2:
        def readinto(self, dest):
            return test_select_mutated()
        def close(self):
            pass
    import select
    # case 1: reading
    a = [F(), F2()]
    selects_eq(select.select([x for x in a], [], []), ([], [], []))
    # case 2: writing
    a = [F2(), F()]
    selects_eq(select.select([], [x for x in a], []), ([], [], []))
    # case 3: both
    a = [F(), F2()]
    selects_eq(select.select([x for x in a], [x for x in a], []), ([], [], []))

class MySocket(object):

    class error(Exception):
        pass
    error = error()

    def __init__(self, bufsize=0):
        self.send_data = []
        self.
