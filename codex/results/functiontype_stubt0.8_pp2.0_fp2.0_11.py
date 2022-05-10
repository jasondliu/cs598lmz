from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
type(a)

type(a) == GeneratorType
type(a) == FunctionType
type(b) == list

def x(): yield 1
g = x()
type(g)
type(g) == GeneratorType
type(g) == FunctionType
type(x) == FunctionType
 
import inspect
print(inspect.getgeneratorstate(g))
next(g)
print(inspect.getgeneratorstate(g))
try:
    next(g)
except StopIteration:
    print('done!')
print(inspect.getgeneratorstate(g))
print(inspect.getgeneratorstate(g))
x = [1, 2, 3]
for y in x:
    print(y)
    y += 1
x
def f():
    x = [1, 3, 4]
    for y in x:
        print(y)
        y += 1
f()
x
x = [1, 2, 3]
y = iter(x)
while True:
   
