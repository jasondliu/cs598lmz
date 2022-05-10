gi = (i for i in ())
# Test gi.gi_code is None
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Verify that "code" is actually an unbound method.
print(gc.is_tracked(gi.gi_code))
print(gi.gi_code.__name__)

code = gi.gi_code

# Verify that there's some kind of reference to the function object
# somewhere inside the code object, so it stays alive despite being
# unreachable from Python code.
import gc
gc.collect()
if not gc.is_tracked(code):
    print('unexpected')

# Check that it's not the same as the code object for a func
def func(): pass
import inspect
ci = inspect.getcode(func)
print(ci is not code)

# Check what we get from a builtin function: PyEval_EvalFrameEx for
# CPython 3+, and a wrapper for CPython 2.
import binascii
ci = inspect.getcode(binascii.crc32)
print
