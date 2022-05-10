from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'f') for x in range(10))

# 使用默认值
def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)

# 可变参数
def spam(a, b=42, *args):
    print(a, b, args)

spam(1)
spam(1, 2, 3)
spam(1, 2, 3, 4)

# 关键字参数
def spam(a, b=42, *args, c):
    print(a, b, args, c)

spam(1, 2, 3, 4, c=5)

# 命名关键字参数
def spam(a, b=42, *, c):
    print(a, b, c)

spam(1, c=3)

# 参数解
