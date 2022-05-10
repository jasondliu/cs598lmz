import types
# Test types.FunctionType
def someFunction(a,b):
    print "Function called with %d arguments" % len(arguments)

if type(someFunction) == types.FunctionType:
    print "Some Function is a function"

# Test types.LambdaType
someLambda = lambda x: x*x
if type(someLambda) == types.LambdaType:
    print "Some Lambda is a lambda"

# Test types.GeneratorType
def someGenerator():
    yield 1
    yield 2
    yield 3

if type(someGenerator()) == types.GeneratorType:
    print "Some Generator is a generator"

# Test types.DictionaryType
someDict = {'a':1,'b':2,'c':3,'d':4}
if type(someDict) == types.DictionaryType:
    print "Some Dict is a dictionary"

# Test types.IntType
someInt = 1
if type(someInt) == types.IntType:
    print "Some Int is an integer"

# Test types.LongType
