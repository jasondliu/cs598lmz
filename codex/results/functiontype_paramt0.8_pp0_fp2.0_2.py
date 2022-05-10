from types import FunctionType
list(FunctionType(fn2.func_code, {}))

a= list(fn2)
print a

a= fn2()
print a

for x in fn2():
    print x**3


#range(1, 5)
#range(10)
#range(5)
#range(0, 10, 2)


# xrange()

print range(10)
print xrange(10)

l1 = [1, 2, 3]
l2 = [10, 20, 30]
print zip(l1, l2)
print dict(zip(l1, l2))

print type(xrange(1, 10, 2))

def fn3(n):
    for x in xrange(n):
        yield x**3

print type(fn3(10))

for x in fn3(10):
    print x


s = 'aAaA'
print s.find('A')
print s.find('A', 2)
print s.find('A', 3)
print s.find('A', 4)
print s.
