from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, type))

#<class 'generator'>
#True
#False
#False

# generator 生成器
# 调用函数的时候，函数内部的代码不会执行，当生成器调用的时候，会执行内部代码，遇到yield就返回，再次执行，就从上次返回的yield后面继续执行
def gen():
    print("ok")
    yield 1
    print("ok2")
    yield 2
    print("ok3")

g = gen()
print(next(g))
print
