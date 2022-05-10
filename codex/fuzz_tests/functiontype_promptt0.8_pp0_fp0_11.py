import types
# Test types.FunctionType if broken
class Broken(object):
    pass
def test_broken():
    raise Broken()
broken = types.FunctionType(test_broken.func_code, {})
try:
    broken()
except Broken:
    pass
else:
    print 'subinterpreters: types.FunctionType is broken'

# Test repr() on those objects, to check that repr()s are independent
# between subinterpreters
import sys
res = api.run_string('import types; repr(types.FunctionType)')
print res
if res[0]:
    raise res[1]
if res[1] == eval('repr(types.FunctionType)', {}):
    print 'subinterpreters: repr(types.FunctionType) not independent'
res = api.run_string('import sys; repr(sys)')
print res
if res[0]:
    raise res[1]
if res[1] == eval('repr(sys)', {}):
    print 'subinterpreters: repr(sys) not independent'

# Test objects with a custom __repr__()
