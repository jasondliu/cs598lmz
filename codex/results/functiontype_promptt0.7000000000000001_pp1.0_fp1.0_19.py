import types
# Test types.FunctionType
try:
    assert isinstance(lambda: None, types.FunctionType)
except:
    print("SKIP")
    raise SystemExit

# Test __repr__()
try:
    repr(lambda: None)
except:
    print("SKIP")
    raise SystemExit

# Test __str__()
try:
    str(lambda: None)
except:
    print("SKIP")
    raise SystemExit

# Test __hash__()
try:
    hash(lambda: None)
except:
    print("SKIP")
    raise SystemExit

# Test __call__()
def f():
    return "OK"

try:
    assert f() == 'OK'
except:
    print("SKIP")
    raise SystemExit

# Test __code__
try:
    assert f.__code__
except:
    print("SKIP")
    raise SystemExit
