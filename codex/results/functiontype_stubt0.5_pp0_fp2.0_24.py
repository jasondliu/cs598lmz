from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 定义一个函数
def test():
    print("test")

# 定义一个函数
def test1():
    print("test1")

a = test
print(isinstance(a, FunctionType))

# 定义一个函数
def test2():
    print("test2")

# 定义一个函数
def test3():
    print("test3")

a = test2
b = test3
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# 定义一个函数
def test4():
    print("test4")

# 定义一个函数
def test5():
    print("test5")

a = test4
b = test5
c = test4
print(isinstance(a,
