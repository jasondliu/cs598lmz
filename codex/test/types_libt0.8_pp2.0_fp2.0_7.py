import types
types.FunctionType
def square(x):
    return x*x
f=square(5)
print(square)
print(f)

f=abs;
print(f)
print(f(-10))

def add(x,y,f):
    return f(x)+f(y);

print(add(-5,-6,abs))

def f(x):
    return x*x;

r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5]))

def fn(x,y):
    return x*10+y
print(reduce(fn,[1,2,3,4,5]))

