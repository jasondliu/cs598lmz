gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_frame.f_lasti

## LANGUAGE FEATURE ##

# Test function annotations
def f(a: 'annotation'):
    return a

# Test class annotations
class C:
    pass

# Test __annotations__
C.__annotations__

# Test __doc__
def f():
    'doc'

f.__doc__

# Test __module__
def f():
    pass

f.__module__

# Test __qualname__
def f():
    pass

f.__qualname__

# Test locals()
locals()

# Test globals()
globals()

# Test __package__
__package__

# Test __loader__
__loader__

# Test __spec__
__spec__

# Test __file__
__file__

# Test __cached__
__cached__

# Test __name__
__name__

# Test __builtins__
__builtins__

## TYPES ##

# Test NoneType
