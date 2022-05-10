import types
# Test types.FunctionType
try:
    f = foo(lambda x: x)
except TypeError as exc:
    print("TypeError caught: %s" % str(exc))
except NameError as exc:
    if str(exc) != "global name 'foo' is not defined":
        raise
    
# Non-leninear sanity check
if foo([1,2,3]) != [1,2,3]:
    raise "Test wrong!"

if foo(lambda x: x(lambda x: x))(foo) != foo:
    raise "Test wrong!"

a = []
if foo(a + [lambda x: foo(x)])(lambda x: x * 2) != [lambda x: foo(x), lambda x: foo(x)]:
    raise "Test wrong!"

# Test enumerate, map and filter
x = 1
y = 2
try:
    z = foo(enumerate)(map)(foo)(filter)
except TypeError as exc:
    print("TypeError caught: %s" % str(exc))
except NameError as exc:
    if str(exc)
