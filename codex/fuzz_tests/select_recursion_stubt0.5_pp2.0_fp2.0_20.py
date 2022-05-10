import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    assert a == [1]

class TestSelect:

    def test_error_conditions(self):
        # select() should raise ValueError if the arguments are not sequences
        # or if they contain non-numeric objects
        self.assertRaises(ValueError, select.select, 1, 2, 3)
        self.assertRaises(ValueError, select.select, [1], [2], [3])
        self.assertRaises(ValueError, select.select, [1], [2], [3])
        self.assertRaises(ValueError, select.select, [1], [2], [3])
        self.assertRaises(ValueError, select.select, [1], [2], [3])
        self.assertRaises(ValueError, select.select, [1], [2], [3])
        self.assertRaises(ValueError, select.select, [1], [2], [3])
        self.assertRaises(ValueError, select.select
