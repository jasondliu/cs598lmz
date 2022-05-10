import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            a.append(1)

    select.select([F()], [], [], 0)
    assert a == [1]

class SelectTests(unittest.TestCase):

    def test_error_conditions(self):
        self.assertRaises(ValueError, select.select, [], [], [], -1)

        class Bogus(object):
            def fileno(self):
                return 'ham'
        self.assertRaises(TypeError, select.select, [Bogus()], [], [])

        class Bogus2(object):
            def fileno(self):
                return object()
        self.assertRaises(TypeError, select.select, [Bogus2()], [], [])

        class Bogus3(object):
            def fileno(self):
                return 5
            def __int__(self):
                raise TypeError
        self.assertRaises(TypeError, select.select, [Bogus3()], [], [])

    def test_select(self):
        cmd = 'for i in 0
