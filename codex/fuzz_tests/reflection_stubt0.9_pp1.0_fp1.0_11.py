fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


def to_raise(e):
    raise e

class ReprWrapper(Exception):
    def __init__(self, obj):
        self.obj = obj
    def __repr__(self):
        return repr(self.obj)

class ExceptionTest(unittest.TestCase):

    def test_str(self):
        class MyException(Exception):
            pass
        msg = "the message"
        exc = MyException(msg)
        self.assertEqual(str(exc), msg)
        self.assertEqual(msg.__class__, str)

    def test_str_and_instance_args(self):
        class MyException(Exception):
            def __str__():
                return "str"
            def __init__(self, args=None):
                self.args = args
        x = MyException()
        self.assertEqual(x.args, None)
        x = MyException(1)
        self.assertEqual(x.args, 1)

    def test_repr(self
