import types
# Test types.FunctionType
code = compile('''def func():
        print "Oops!"
        return None''', '<string>', 'exec')
fun = types.FunctionType(code.co_consts[0], globals(), 'newfunc')
fun()

# Test types.GeneratorType
#tests for generator objects

def build_generator(lst):
    for item in lst:
        yield item

iterable = build_generator([1,2,3])
assert type(iterable) == types.GeneratorType
try:
    iterable.__name__
except AttributeError:
    print "No .__name__ attribute for GeneratorType"

try:
    iterable.__module__
except AttributeError:
    print "No .__module__ attribute for GeneratorType"

try:
    iterable.__doc__
except AttributeError:
    print "No .__doc__ attribute for GeneratorType"

try:
    iterable.__dict__
except AttributeError:
    print "No .__dict__ attribute for GeneratorType"


#
