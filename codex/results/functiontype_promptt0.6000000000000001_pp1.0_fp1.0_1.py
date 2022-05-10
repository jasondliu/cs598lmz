import types
# Test types.FunctionType
try:
    from types import FunctionType
    FunctionType
except:
    print "SKIP"
    raise SystemExit

# Test type()
try:
    type
except:
    print "SKIP"
    raise SystemExit

def f():
    pass

print type(f)
print type(type)

# Test isinstance()
try:
    isinstance
except:
    print "SKIP"
    raise SystemExit

print isinstance(f, FunctionType)
print isinstance(type, FunctionType)

# Test issubclass()
try:
    issubclass
except:
    print "SKIP"
    raise SystemExit

print issubclass(FunctionType, type)
print issubclass(type, FunctionType)
