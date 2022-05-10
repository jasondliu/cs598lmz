fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# Test that the code object is not pickled.
import pickle
try:
    pickle.dumps(fn.__code__)
except TypeError:
    print('TypeError')

# Test that the code object is not marshalled.
import marshal
try:
    marshal.dumps(fn.__code__)
except ValueError:
    print('ValueError')
