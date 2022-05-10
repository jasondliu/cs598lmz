import types
# Test types.FunctionType type
testType("FunctionType", types.FunctionType, FunctionType)

## Test the GlobalFunction class

# Test GlobalFunction.__call__
# Grab a dummy function from the module
testFunc = TestFunction

# Check function without arguments
test("GlobalFunction.__call__ (no kwargs)", TestFunction, testFunc())

# Check function with arguments
test("GlobalFunction.__call__ (with kwargs)", TestFunction, testFunc(1,2,3,4,five=5))

# Test GlobalFunction.__str__
print "GlobalFunction:", TestFunction

# Test GlobalFunction.__repr__
print "GlobalFunction (repr):", repr(TestFunction)

# Test GlobalFunction.__cmp__
test("GlobalFunction.__cmp__", TestFunction, TestFunction)
test("GlobalFunction.__cmp__", TestFunction, TestFunction2)

# Test GlobalFunction.__nonzero__
test("GlobalFunction.__nonzero__", True, bool(TestFunction))

# Test GlobalFunction.__hash__
hash(TestFunction)


