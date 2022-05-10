from types import FunctionType
list(FunctionType() for _ in range(10))

def g():
    print("xxx")
g.__name__ = "hello"
print(g.__name__)

g()

#变量作用域
#全局作用域
name = "python"
def f1():
    print(name)
f1()

#局部作用域
def f2():
    name = "java"
    print(name)
f2()
#内嵌作用域
def f3():
    def inner():
        print(name)
    inner()
f3()

#全局变量
name = "python"
def f4():
    name = "java"
    def inner():
        name = "c++"
        print(name)
    inner()
f4()
print(name)

#局部变量
name = "python"
def f5():
    name = "java"
   
