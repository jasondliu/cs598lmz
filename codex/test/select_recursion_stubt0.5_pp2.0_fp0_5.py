import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return len(a)

    f = F()
    a.append(f)
    r, w, x = select.select([f], [], [], 1)
    assert r == [f]
    assert a == [f]


class TestSelect(unittest.TestCase):

    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, [], [], [], -1)
        self.assertRaises(TypeError, select.select, 1, 2, 3)
        self.assertRaises(TypeError, select.select, [1], [2], [3])
        self.assertRaises(TypeError, select.select, [], [], [], "foo")
        self.assertRaises(TypeError, select.select, [], [], [], 1, 2)

    def test_returned_list_identity(self):
        # See issue #8326
        r, w, x = select.select([], [], [], 1)
        self.assertTrue(r is not [])
