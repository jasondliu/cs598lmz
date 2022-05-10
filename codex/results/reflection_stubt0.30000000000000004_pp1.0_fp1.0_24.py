fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# __code__ is not a code object
try:
    fn.__code__ = 1
except TypeError:
    print('TypeError')

# __code__ is not a code object
try:
    fn.__code__ = 'abc'
except TypeError:
    print('TypeError')

# __code__ is not a code object
try:
    fn.__code__ = {}
except TypeError:
    print('TypeError')

# __code__ is not a code object
try:
    fn.__code__ = []
except TypeError:
    print('TypeError')

# __code__ is not a code object
try:
    fn.__code__ = object()
except TypeError:
    print('TypeError')

# __code__ is not a code object
try:
    fn.__code__ = object
except TypeError:
    print('TypeError')

# __code__ is not a code object
try:
    fn.__code__ = type
except TypeError:
    print('TypeError')

# __code
