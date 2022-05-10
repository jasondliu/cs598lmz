from types import FunctionType
list(FunctionType(addition.__code__,globals())(3,8))

#nested function
def outer():
    x=5
    def inner():
        nonlocal x
        x+=1
        return x
    return inner
f=outer()
f()
f()
#closure
def outer2(x):
    def inner2():
        nonlocal x
        x+=1
        return x
    return inner2
f=outer2(10)
f()
f()
#nonlocal
def outer3():
    x=5
    def inner3():
        global x
        x+=1
        return x
    return inner3
f=outer3()
f()
f()
x
#generators
def generate_squares(n):
    for i in range(n):
        yield i**2
gen=generate_squares(5)
list(gen)
#generators are iterators and can be used in comprehensions
l=[x**2 for x in range(5)]
g=(x**2 for x in range(5))
#generators can
