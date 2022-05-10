import types
types.ClassType

# The following code is a simple example of how you can use the
# types module to check if an object is of a certain type.

def displayNumType(num):
    print num, 'is',
    if type(num) == types.IntType:
        print 'an integer'
    elif type(num) == types.FloatType:
        print 'a float'
    elif type(num) == types.ComplexType:
        print 'a complex number'
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')

# Here's a quick example of how you can use the types module to test
# whether an object is a function or not.

def testFuncType(obj):
    if type(obj) == types.FunctionType:
        print obj, 'is a function'
    else:
        print obj, 'is not a function
