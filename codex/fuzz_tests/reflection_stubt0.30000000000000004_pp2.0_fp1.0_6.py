fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# This is a bit of a hack, but it lets us use the same test code for both
# CPython and PyPy.
class FakeFrame(object):
    def __init__(self, f_code):
        self.f_code = f_code

class TestTraceback(unittest.TestCase):

    def test_extract_tb(self):
        try:
            raise ValueError
        except:
            tb = sys.exc_info()[2]
            stack = traceback.extract_tb(tb)

        # Check some aspects of the return value
        self.assertEqual(len(stack), 1)
        filename, lineno, name, line = stack[0]
        self.assertTrue(filename.endswith('test_traceback.py'))
        self.assertEqual(name, 'test_extract_tb')
        self.assertTrue(line.startswith('            raise ValueError'),
                        'got %r' % line)
