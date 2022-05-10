import types
types.MethodType(func1, None, int)
types.MethodType(func1, 10, int)

def func2(self):
	print(self)

def func3(self):
	print(self)


def func4(self):
	print(self)

a = func2.__get__(10)
b = func2.__get__(20, int)
# print(func2.__get__(30, int))
# print(b)

# isinstance(a, int)

a = {'name': 'ss'}
func3.__get__(a, type(a))

# a.func3()
# print(a)
# help(type(a))
