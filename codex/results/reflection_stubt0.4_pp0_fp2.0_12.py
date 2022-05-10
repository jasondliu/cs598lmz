fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    fn()
except TypeError:
    print('TypeError')

# __code__ must be a code object
gi = (i for i in ())
try:
    gi.__code__ = 5
except TypeError:
    print('TypeError')

# __code__ must be a code object
gi = (i for i in ())
try:
    gi.__code__ = 'string'
except TypeError:
    print('TypeError')

# __code__ must be a code object
gi = (i for i in ())
try:
    gi.__code__ = {}
except TypeError:
    print('TypeError')

# __code__ must be a code object
gi = (i for i in ())
try:
    gi.__code__ = []
except TypeError:
    print('TypeError')

# __code__ must be a code object
gi = (i for i in ())
try:
    gi.__code__ = None
except TypeError:
    print('TypeError')

# __code__ must
