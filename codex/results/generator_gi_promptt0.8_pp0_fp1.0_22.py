gi = (i for i in ())
# Test gi.gi_code.co_filename. See also issue #14308.
dir(gi)
dir(gi)
dir(gi.gi_code)


def read_value_from_stack(stack, pos, expected_type):
    pass


class Traceback_Test(unittest.TestCase):
    def test_traceback(self):
        import traceback, sys, StringIO
        try:
            raise ValueError
        except:
            e, b, t = sys.exc_info()

            stio = StringIO.StringIO()
            traceback.print_tb(t, file=stio)
            self.assertEqual(stio.getvalue(), '  File "test_traceback.py", line 20, in test_traceback\n    raise ValueError\n')

            stio = StringIO.StringIO()
            traceback.print_tb(t, None, stio)
            self.assertEqual(stio.getvalue(), '  File "test_traceback.py", line 20, in test_traceback\n    raise ValueError\n')
