fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Implicit exception
try:
    fn()
except TypeError as e:
    print(e)

# Explicit exception
try:
    fn.__code__.gi_code
except AttributeError as e:
    print(e)
