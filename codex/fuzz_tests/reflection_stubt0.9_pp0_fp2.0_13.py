fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

try:
    del fn
except TypeError as e:
    print(repr(e))

try:
    del fn.__code__
except TypeError as e:
    print(repr(e))

try:
    del fn.__code__.gi_running
except AttributeError as e:
    print(repr(e))
