from types import FunctionType
list(FunctionType(lambda x: x**2, globals()).__code__.co_freevars)

#定义一个闭包
def make_power(y):
    def power(x):
        return x ** y
    return power
f = make_power(2)
print(f(5))
print(make_power(2)(5))
f2 = make_power(3)
print(f2(3))
print(make_power(3)(3))
