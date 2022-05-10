fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test __code__ is not writable
try:
    fn.__code__ = None
except TypeError:
    print('TypeError')

# Test __code__ is not writable
try:
    del fn.__code__
except TypeError:
    print('TypeError')

# Test __code__ is not writable
try:
    fn.__code__ = 1
except TypeError:
    print('TypeError')

# Test __code__ is not writable
try:
    del fn.__code__
except TypeError:
    print('TypeError')

# Test __code__ is not writable
try:
    fn.__code__ = 'str'
except TypeError:
    print('TypeError')

# Test __code__ is not writable
try:
    del fn.__code__
except TypeError:
    print('TypeError')

# Test __code__ is not writable
try:
    fn.__code__ = b'bytes'
except TypeError:
    print('TypeError')

#
