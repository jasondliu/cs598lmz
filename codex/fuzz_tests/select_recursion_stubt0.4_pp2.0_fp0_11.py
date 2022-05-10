import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return a.pop()

    select.select([F()], [], [], 0)

class TestSelect:
    def test_error_conditions(self):
        # select() should raise ValueError if passed empty lists
        self.assertRaises(ValueError, select.select, [], [], [])

        # but some platforms (Solaris) seem to return nothing instead
        for w, x, y in [([], [], []), ([], [1], []), ([1], [], [])]:
            self.assertTrue(not select.select(w, x, y) or
                            (w, x, y) == ([1], [], []))

        # select() should raise TypeError if passed a non-list
        self.assertRaises(TypeError, select.select, 1, 2, 3)

        # select() should raise TypeError if passed lists with non-integers
        self.assertRaises(TypeError, select.select, [1, 2], [], [])
        self.assertRaises(TypeError, select.select, [], [1, 2
