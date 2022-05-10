import types
# Test types.FunctionType()
def foo(x):	# 定义函数 foo()
	return x
foo(3)			# 执行函数
print(type(foo))		# 查看 foo 函数的类型
print(isinstance(foo,types.FunctionType))	# 查看 foo 是否为类型 FunctionType() 的对象
#print(type(foo).__class__)	
print('-------------')

# Test  types.LambdaType()
func = lambda x:print(x)	# lambda 来定义的函数
func(123)
print(type(func))
print(isinstance(func,types.LambdaType) )	# 查看 func 是否为类型 LambdaType() 的对象

# Test types.GeneratorType()
def fn():
	yield 9
gen = fn()
