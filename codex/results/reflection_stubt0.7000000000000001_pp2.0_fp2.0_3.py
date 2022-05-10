fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
try:
    print(fn())
except TypeError as e:
    print(e)

def fn():
    def _fn(i):
        return i
    return _fn
fn().__code__ = None
try:
    print(fn()(42))
except TypeError as e:
    print(e)

f = float
try:
    f.__code__ = None
except TypeError as e:
    print(e)

try:
    f.__code__ = f.__code__
except TypeError as e:
    print(e)

print(f.__code__ is type(f).__code__)

try:
    f.__code__ = type(f).__code__
except TypeError as e:
    print(e)

try:
    f.__code__ = type(f).__code__.__class__.__code__
except TypeError as e:
    print(e)

try:
    f.__code__ = (lambda: None).__code__
except TypeError as e
