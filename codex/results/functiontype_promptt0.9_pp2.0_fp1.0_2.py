import types
# Test types.FunctionType()
def func1():
	pass

def func2():
	pass

print "Result of types.FunctionType(func1): ", types.FunctionType(func1)
# Result of types.FunctionType(func1):  <type 'function'>
print "Result of func1.__class__: ", func1.__class__
# Result of func1.__class__:  <type 'function'>
print "Result of type(func2): ", type(func2)
# Result of type(func2):  <type 'function'>
print "Result of func2.__class__: ", func2.__class__
# Result of func2.__class__:  <type 'function'>
"""
exit()

#Test out types.FunctionType() method
def func1(a, b=5):
	print "First argument: ", a, " and second argument: ", b

print "Result of type(func1) is: ", type(func1)
# Result of type(func1) is:  <type 'function'>
print "Result of func1.__class__ is:
