import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)

def square(a):
	return a * a

square_func = FUNTYPE(square)
print(square_func(5))

# 闭包
def outer(a):
	def inner(b):
		return a * b
	return inner

print(outer(4)(2))


# 装饰器 闭包的一种特殊应用
def make_pretty(func):
	def inner():
		print('I got decorated')
		func()
	return inner

def ordinary():
	print('I am ordinary')

pretty = make_pretty(ordinary)
pretty()

# 下面这种写法是等价的
@make_pretty
def ordinary():
	print('I am ordinary')

def decorate(func):
	def inner(*args, **kwargs):
		print('start')
		
