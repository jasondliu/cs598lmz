import types
types.MethodType(lambda self: self.name, None)

# 任意数量参数
def arbitrary_param(name, *numbers):
    print(name)
    print(numbers)
arbitrary_param('dog', 1, 2, 3)

# 任意数量关键字参数
def arbitrary_key_param(name, **kw):
    print(name)
    print(kw)
arbitrary_key_param('dog', a = 1, b = 2)

# 命名关键字参数
def named_params(name, *, city, job):
    print(name, city, job)
named_params('dog', city = 'beijing', job = 'engineer')

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
fact(5)

# 尾递归优
