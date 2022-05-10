fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'

# This is the only way to get a code object from a generator
# object in Python 3.
def get_code_object(gen):
    return gen.gi_code

class TestGenerator(unittest.TestCase):
    def test_simple_generator(self):
        def simple_generator():
            yield 1
            yield 2
            yield 3

        sg = simple_generator()
        self.assertEqual(next(sg), 1)
        self.assertEqual(next(sg), 2)
        self.assertEqual(next(sg), 3)

    def test_generator_with_args(self):
        def generator_with_args(x):
            yield x
            yield x + 1
            yield x + 2

        gwa = generator_with_args(1)
        self.assertEqual(next(gwa), 1)
        self.assertEqual(next(gwa), 2)
        self.assertEqual(next(gwa), 3)


