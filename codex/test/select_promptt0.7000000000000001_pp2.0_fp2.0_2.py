import select
# Test select.select
class SelectTest(unittest.TestCase):
    def testSelect(self):
        self.assertEqual(select.select([], [], [], 0.0), ([], [], []))

class OptionsTest(unittest.TestCase):
    def test_options(self):
        self.assertTrue(hasattr(select, 'PIPE_BUF'))
        self.assertTrue(hasattr(select, 'STDERR_FILENO'))
        self.assertTrue(hasattr(select, 'STDIN_FILENO'))
        self.assertTrue(hasattr(select, 'STDOUT_FILENO'))
        self.assertTrue(hasattr(select, 'O_NONBLOCK'))

class FDListTests(unittest.TestCase):
    def setUp(self):
        self.r, self.w = os.pipe()

    def tearDown(self):
        os.close(self.r)
        os.close(self.w)

