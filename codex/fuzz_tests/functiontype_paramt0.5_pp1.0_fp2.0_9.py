from types import FunctionType
list(FunctionType(lambda x: x,globals())(x) for x in range(10))

# 方法二
# 利用lambda表达式创建一个匿名函数，然后调用map()函数
list(map(lambda x: x, range(10)))

# 方法三
# 利用生成器表达式
list(x for x in range(10))

# 方法四
# 利用生成器函数
def gen():
    for x in range(10):
        yield x
list(gen())

# 方法五
# 利用生成器函数
list(x for x in range(10))

# 方法六
# 利用生成器函数
list(x for x in range(10
