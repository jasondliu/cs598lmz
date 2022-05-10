import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
        def close(self):
            pass

    try:
        select.select([F()], [], [])
    except RuntimeError as e:
        assert str(e).startswith('unexpected m_state')
    except:
        assert False, 'expected RuntimeError, got %s' % (sys.exc_info()[0],)

class FooTest(unittest.TestCase):
    def test_foo(self):
        assert False

class FooTest2(TestCase):
    def test_foo(self):
        assert False


class Test_unittest(TestCase):
    def test_class(self):
        self.assertFalse(unittest.TestSuite())
        self.assertFalse(unittest.TestSuite([]))
        self.assertFalse(unittest.TestSuite([FooTest]))

    def test_inst(self):
        self.assertFalse(unittest.TestSuite(FooTest()))

    def test_testcase(self):
        self.assertFalse(unittest.Test
