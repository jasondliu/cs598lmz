import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    f = F()
    select.select([f], [], [])

def test_bug_56466a(self):
    # SF 56466
    # Testing that select.select raises a ValueError if
    # any file descriptor is negative
    self.assertRaises(ValueError, select.select, [-1], [], [])
    self.assertRaises(ValueError, select.select, [], [-1], [])
    self.assertRaises(ValueError, select.select, [], [], [-1])

def test_bug_56466b(self):
    # Testing that select.select raises a ValueError if
    # any file descriptor is greater or equal to FD_SETSIZE
    self.assertRaises(ValueError, select.select, [select.FD_SETSIZE], [], [])
    self.assertRaises(ValueError, select.select, [], [select.FD_SETSIZE], [])
    self.assertRaises(ValueError, select.select, [], [], [select.FD_SETSIZE
