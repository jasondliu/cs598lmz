import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)


class TestSelect(unittest.TestCase):
    def test_error_conditions(self):
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [1], 2, 3)
        self.assertRaises(TypeError, select.select, [1], [2], 3)
        self.assertRaises(TypeError, select.select, [1], [2], [3], "four")
        self.assertRaises(TypeError, select.select, [1], [2], [3], 4, 5)
        self.assertRaises(ValueError, select.select, [], [], [], -1)
        self.assertRaises(ValueError, select.select, [], [], [], -1.0)

