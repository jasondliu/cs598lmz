from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))


def f1(x, y=6):
    return x + y
print(f1.__code__)
print(f1.__code__.co_argcount)
print(f1.__code__.co_varnames)
print(f1.__code__.co_consts)
print(f1.__code__.co_names)
print(f1.__code__.co_filename)
print(f1.__code__.co_nlocals)
print(f1.__code__.co_firstlineno)
print(f1.__code__.co_lnotab)

# 函数的调用
def my_function():
    print("hello, world")

my_function()
my_function = print
my_function(1,2,3, sep='*')

print(len)
print(len([]))

# 可变参数和不可变参
