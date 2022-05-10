import types
types.FunctionType

def add(x, y):
    return x + y

print(type(add))

# 创建一个函数
def say_hello():
    print('hello world')

say_hello()

# 函数返回值
def add(x, y):
    return x + y

print(add(1, 2))

# 函数参数
def add(x, y):
    return x + y

print(add(1, 2))

# 函数参数默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 3))

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
   
