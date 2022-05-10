gi = (i for i in ())
# Test gi.gi_code raises SystemError: iterator gi already executing
try:
    inspect.getgeneratorlocals(gi)
except SystemError:
    print('SKIP')
    raise SystemError

# code object is not implemented in MicroPython
d = (yield from [1, 2])
