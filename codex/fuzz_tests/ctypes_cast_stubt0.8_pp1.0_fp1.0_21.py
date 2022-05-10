import ctypes
ctypes.cast(fn("hello"), ctypes.c_void_p)

def my_func(x):
    return (x ** 2)

def f(my_func):
    return my_func(x)

x = 2
print(f(my_func))

fs = (lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4)
fxs = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in fs:
    print(f(2))
print()

for xx in range(5):
    for fx in fxs:
        print(fx(xx))

print()
print(fxs)

def hi():
    print("hi")

def bye():
    print("bye")

functions = [hi, bye]

for function in functions:
    function()
print()

class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hi, my name is
