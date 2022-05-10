from types import FunctionType
a = (x for x in [1])
x = [1]
b = (x for x in range(10))
c = (x for x in range(10))
print(type(b))
print(type(c))
print(b is c)
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))
print(b == c)
print(a == c)


def greet(name):
    print("hello, ", name)


def bye():
    print("bye")


def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper


new_fun = decorator(greet)

new_fun("a")
new_fun("b")
new_fun("c")

print("*" * 20)
new_fun2 = decorator(bye)

new_fun2()
