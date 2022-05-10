from types import FunctionType
list(FunctionType(lambda x, y: x+y, globals(), "add")(1, 2))

def add(x, y):
    return x + y

print(add(1, 2))

# 可以通过__code__属性获取函数的原始字节码信息
add.__code__

# 也可以通过__code__属性修改函数的原始字节码信息
def sub(x, y):
    return x - y

add.__code__ = sub.__code__
print(add(1, 2))

# 可以通过__defaults__属性获取函数的默认参数值
def add(x, y=1):
    return x + y

add.__defaults__

#
