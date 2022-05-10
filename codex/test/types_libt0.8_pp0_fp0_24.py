import types
types.MethodType

# 定义一个函数，返回函数名
def fn(fn):
    return fn

def foo(name):
    return 'hello,' + name

# 给函数变量增加属性
foo.name = 'my_name'
# 将foo函数变量赋值给fn函数
f = fn(foo)
print(f,f.name)


# 给函数动态指定属性
foo.age = 18
print(hasattr(foo, 'age'))
print(foo.age)

# 动态指定属性
setattr(foo, 'level', 'vip')
print(getattr(foo, 'level'))

setattr(foo, 'name', 'new_name')
print(foo.name)

# 给foo
