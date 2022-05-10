from types import FunctionType
a = (x for x in [1])
b = (y for y in range(10))
print(type(a), type(b))
print(isinstance(a, GeneratorType), isinstance(b, GeneratorType))
#print(next(a), next(b))
print(a.__next__(), b.__next__())
print(a.__next__(), b.__next__())

def c():
	print('Start...')
	x = yield 1
	print(x)
	y = yield 2
	print(y)
	z = yield 3
	print(z)

cc = c()
#f = FunctionType()
print(isinstance(cc, GeneratorType))
print(next(cc))
print(cc.send(10))
print(cc.send(20))
print(cc.send(30))

#print(next(cc))
#print(next(cc))
#print(next(cc))
