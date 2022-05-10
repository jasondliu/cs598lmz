import types
types.MethodType(method, object)

#装饰器
def dec(func):
	def in_dec(*arg):
		if len(arg)==0:
			return 0
		for val in arg:
			if not isinstance(val, int):
				return 0
		return func(*arg)
	return in_dec

@dec
def my_sum(*arg):
	return sum(arg)

print(my_sum(1,2,3,4))
print(my_sum(1,2,3,'a'))

#偏函数
int2 = functools.partial(int, base=2)

int2('10010')
