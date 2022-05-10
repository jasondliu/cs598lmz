import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return 0

        def read(self, *args):
            f = F()
            a.append(f)
            return f.read(*args)

    f = F()
    a.append(f)
    try:
        select.select([f], [], [])
    except ValueError:
        pass
    else:
        assert False, "a.read() mutated the list while select() was working"

class TestSelect:
    def test_select(self):
        # Issue #10458: select() should not raise an exception with
        # an empty list
        select.select([], [], [])
        select.select([], [], [], 1)

        # Issue #10458: select() should raise an exception when the
        # timeout is negative
        self.assertRaises(ValueError, select.select, [], [], [], -1)

        # Issue #20531: select() should raise an exception when the
        # timeout is greater than 2**31 - 1
        self.assertRaises(ValueError, select.select, [], [], [],
