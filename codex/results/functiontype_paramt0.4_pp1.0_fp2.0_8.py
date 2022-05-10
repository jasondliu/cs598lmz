from types import FunctionType
list(FunctionType(list.__code__, globals(), "list"))

# 不能使用类的__call__方法
# class List:
#     def __call__(self):
#         print("__call__")
#
# list = List()
# list()

# 装饰器
def deco(func):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print("running target()")

target()

# 函数装饰器
registry = []
def register(func):
    print("running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print("running f1()")

@register
def f2():
    print("running f2()")

def f3():
    print("running f3()")

def main():
    print("running main()")
    print("registry ->", registry)
    f1()
