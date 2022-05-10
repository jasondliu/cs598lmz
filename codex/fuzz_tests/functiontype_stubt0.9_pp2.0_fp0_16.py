from types import FunctionType
a = (x for x in [1])
def b():
	yield 1
print(a, type(a))
print(b, type(b))
print(FunctionType, type(FunctionType))
