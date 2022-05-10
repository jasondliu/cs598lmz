import types
# Test types.FunctionType LambdaType
print(type(lambda x: x+1) == types.LambdaType)
print(type(lambda x: x+1) == types.FunctionType)

# Test types.ClassType
inherit = lambda x: x
print(type(inherit) == types.ClassType)

# Test types.InstanceType
class A:
	def __init__(self, x):
		self.x = x

a = A(3)
print(type(a) == types.InstanceType)

# Test types.MethodType
class B:
	def walk(self):
		print('walk')
		
b = B()
print(type(b.walk) == types.MethodType)

# Test types.UnboundMethodType
def walk(self):
	print('walk')

print(type(walk) == types.FunctionType)
print(type(walk) == types.UnboundMethodType)

# Test types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(
