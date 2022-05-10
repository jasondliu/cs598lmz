import types
types.FunctionType

# 创建一个函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 定义空函数
def nop():
    pass

# 定义一个什么事也不做的空函数，可以用来作为占位符，比如后面需要递归函数的写法
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
# 如果想要一个函数占个位置，不要报错，可以用
