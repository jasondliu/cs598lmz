import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())

    select.select(a, [], [])


class TestSelect(unittest.TestCase):
    def test_error_conditions(self):
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [], 'foo', [])
        self.assertRaises(TypeError, select.select, [], [], 'foo')
        self.assertRaises(ValueError, select.select, [], [], [], -1)
        self.assertRaises(TypeError, select.select, [], [], [], {})

    def test_returned_list_identity(self):
        r, w, x = select.select([], [], [], 1.0)
        self.assertTrue(r is not [])
        self.assertTrue(w is not [])
        self.assertTrue(x is not [])

    def test_select(self):
        a, b, c = select.select([], [], [],
