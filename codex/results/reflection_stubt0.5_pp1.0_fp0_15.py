fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 利用__code__的__globals__属性修改全局变量

# 利用__code__的nested_scopes属性访问嵌套作用域
def outer():
    x = 'old x'
    def inner():
        nonlocal x
        x = 'new x'
    inner()
    return x

outer()


def outer():
    x = 'old x'
    def inner():
        x = 'new x'
    inner()
    return x

outer()

# 利用__code__的freevars属性访问闭包变量
def outer():
    x = 'old x'
    def inner():
        return x
    return inner

f = outer()
f()

# 利用__code__的cellvars属性访问嵌
