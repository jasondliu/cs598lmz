import types
# Test types.FunctionType
def testFunction(a, b):
	return a + 2*b

testFunc = testFunction
if type(testFunc)==types.FunctionType:
	print "testFunc is a function"
else:
	print "testFunc is not a function"

def testFunc2(a):
	return a

testFunc2 = testFunc2(3)
if type(testFunc2)==types.FunctionType:
	print "testFunc2 is a function"
else:
	print "testFunc2 is not a function"

# Test types.InstanceType
class Test:
	pass

test = Test()
if type(test)==types.InstanceType:
	print "test is an instance"
else:
	print "test is not an instance"

test = Test
if type(test)==types.InstanceType:
	print "test is an instance"
else:
	print "test is not an instance"

# Test types.MethodType
class Test:
	def __init__(self):
		self
