import types
types.MethodType(method, instance)

# Class
class MyClass:
	def __init__(self):
		pass
	def __repr__(self):
		return "MyClass"
	def method(self):
		pass

# Instance
instance = MyClass()
instance.method()

# Method
method = instance.method
method()

# Unbound method
unbound_method = MyClass.method
unbound_method(instance)

# Bound method
bound_method = types.MethodType(unbound_method, instance)
bound_method()

# Function
def function(*args, **kwargs):
	pass
function()

# Lambda
lambda_function = lambda *args, **kwargs: None
lambda_function()

# Callable
callable(function)
callable(lambda_function)
callable(unbound_method)
callable(bound_method)

# Staticmethod
class MyStaticClass:
	@staticmethod
	def method():
		pass

static_method = MyStaticClass.method

