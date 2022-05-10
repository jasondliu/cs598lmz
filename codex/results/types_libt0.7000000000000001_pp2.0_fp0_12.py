import types
types.MethodType
types.FunctionType

class A:
	pass

def fn(self):
	print("fn")

a = A()
a.fn = types.MethodType(fn, a)
a.fn()

A.fn = types.MethodType(fn, A)
A.fn(a)

a.fn = types.FunctionType(fn.__code__, globals(), "fn", fn.__defaults__, fn.__closure__)
a.fn()

# 反射 - 动态语言允许我们在程序运行时可以修改代码
# 使用反射我们可以在程序运行时动态的修改代码
class A:
	def __init__(self,x):
		self.x = x

	def fn(self):
		print("fn")

a
