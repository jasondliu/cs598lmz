fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# Run tests
for f in [t for t in dir(unittest) if t.startswith("test")]:
    unittest.TestCase.__dict__[f]()

# Run doctests
import doctest
doctest.testmod()
