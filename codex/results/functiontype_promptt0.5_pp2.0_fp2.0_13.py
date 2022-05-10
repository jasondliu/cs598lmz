import types
# Test types.FunctionType
#
# This is a simple test for types.FunctionType.
#
# This test is not exhaustive.

# Check that types.FunctionType exists and has the right type
try:
    f = types.FunctionType
except AttributeError:
    print("SKIP")
    raise SystemExit

if type(f) is not type:
    print("SKIP")
    raise SystemExit

# Check that types.FunctionType is a subtype of object
if not isinstance(f, object):
    print("SKIP")
    raise SystemExit

# Check that types.FunctionType is callable
try:
    f()
except TypeError:
    pass
else:
    print("SKIP")
    raise SystemExit

# Check that types.FunctionType is callable with 1 argument
try:
    f(1)
except TypeError:
    pass
else:
    print("SKIP")
    raise SystemExit

# Check that types.FunctionType is callable with 2 arguments
try:
    f(1, 2)
except TypeError:
    pass
else:
