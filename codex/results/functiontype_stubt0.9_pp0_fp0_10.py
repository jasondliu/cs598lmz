from types import FunctionType
a = (x for x in [1])
print(type(a))

b = list(a)
print(b)

b = [1,2,3,4,5,6,7]
c = filter(lambda n: n % 2 != 0, b)
print(list(c))

def f(l, key):
	return [x for x in l if key(x)]
#filter
b = [1,2,3,4,5,6,7]
c = f(b, lambda n: n % 2 != 0)
print(c)

#map
d = map(lambda n: n * 2 + 5, c)
print(list(d))
