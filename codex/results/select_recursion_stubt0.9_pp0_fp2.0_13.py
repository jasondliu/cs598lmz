import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
    a.append(F())
    while a:
        ret = select.select(a, a, a)
        a.pop()
        assert not ret[0]
        assert not ret[1]
        assert not ret[2]

class TestSelect(unittest.TestCase):

    def test_error_conditions(self):
        # Test bad file descriptor
        self.assertRaises(ValueError, select.select, [42], [], [])

        # Test file descriptor too large
        self.assertRaises(ValueError, select.select, [100000], [], [])

        # Try a mixture of good and bad file descriptors
        self.assertRaises(ValueError, select.select, [sys.__stdout__, 42], [], [])

        # Try bad writeable and _exceptional file descriptors
        self.assertRaises(ValueError,
                          select.select,
                          [sys.__stdout__], [42], [])
        self.assertRaises(ValueError,
                          select.select,
                          [sys
