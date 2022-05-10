fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
callable(fn)

# # TypeError: 'code' object is not iterable

# 使用函数定义方式，也会报错

def fn():
    yield

fn.__code__ = (i for i in ())
callable(fn)
# TypeError: 'code' object is not iterable

# 函数有 __code__ 属性，显示绑定了一个可以迭代的对象

# 函数允许绑定一个 code 对象
# 函数允许改写 code 对象
# 函数允许改写 code 属性
# 函数允许将 code 替换为可迭代对象
#
