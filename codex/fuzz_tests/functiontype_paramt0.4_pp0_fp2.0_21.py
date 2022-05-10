from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

def foo(a,b,c):
    print(a,b,c)

list(foo.__code__.co_varnames)

# 参数类型检查
def foo(a:int, b:str, c:list):
    print(a,b,c)

foo(1,2,3)
foo(1,'2',[3])

# 参数默认值
def foo(a, b=3, c=4):
    print(a,b,c)

foo(1)
foo(1,2)
foo(1,2,3)

# 可变参数
def foo(a, b=3, c=4, *args):
    print(a,b,c,args)

foo(1)
foo(1,2)
foo(1,2,3)
foo(1,2,3,4
