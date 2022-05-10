fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# TypeError: 'generator' object is not callable

# 其他
# 将函数赋值给变量
def foo():
    print('foo')

bar = foo
bar()
# foo

# 将函数作为参数传入
def foo():
    print('foo')

def bar(func):
    func()

bar(foo)
# foo

# 将函数作为返回值返回
def foo():
    print('foo')

def bar():
    return foo

bar()()
# foo

# 将函数作为元素存入容器中
def foo():
    print('foo')

l = [foo]
l[0]()
# foo

# 将函数作为属性绑定到对
