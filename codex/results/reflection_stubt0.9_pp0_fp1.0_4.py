fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())

if __name__ == "__main__":
    import unittest


    def as_gen(g):
        """helper to convert generator-like thing to a real generator"""
        while True:
            try:
                yield next(g)
            except StopIteration:
                break


    class TestCode(unittest.TestCase):
        def test_print(self):
            # Make sure printing code objects works (doesn't crash).
            # A test for bugs 2402 and 6260.
            #
            # Print out code object using a format string for Python 2 and 3.
            co = compile('print(1)\n', '?', 'exec')
            with captured_stdout() as stdout:
                print(('%r' % (co,)).replace('"<code', '"<code object'))

            text = stdout.getvalue().replace('u"<code', '"<code')
            expected = """
<code object <module> at 0x00000243E039F180, file "?", line 1>

