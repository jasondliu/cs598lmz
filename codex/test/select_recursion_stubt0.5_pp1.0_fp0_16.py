import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1

    a.append(F())
    try:
        select.select([], a, [])
    except ValueError:
        pass

class Test_select(unittest.TestCase):
    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, [1], [2], [3], -1)
        self.assertRaises(TypeError, select.select, 1, 2, 3)

    def test_returned_list_identity(self):
        # See issue #14983
        r, w, x = select.select([], [], [], 1)
        self.assertIsNot(r, w)
        self.assertIsNot(r, x)
        self.assertIsNot(w, x)

        r, w, x = select.select([], [], [], 0)
        self.assertIsNot(r, w)
        self.assertIsNot(r, x)
