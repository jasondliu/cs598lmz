from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print a, b
print a.next(), b.next()
print a.next(), b.next()

print a == b, hash(a), hash(b)

def func(x):
    print x
    x.next()
    for i in x:
        print i

func(a)
func(b)

print type(a), type(b)

def func2(x, y):
    print x == y, type(x) == type(y)

func2(a, b)

def func3(x):
    if type(x) == FunctionType:
        print x
        x()

def func4(x):
    print x
    func3(x)

func3(func4)

# functions are objects
# objects are first class members
# functions are first class members

# this is how you could implement a decorator
# usually done with @ syntax
def decorator(f):
    def inner():
        print "before"
        r = f()
       
