fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# 这里我们把 __code__ 设置为 generator，原来的 code 对象被替换掉了，导致 fn 的执行变成了一个 generator 的执行，这个 generator 没有 yield，所以就报错了。
# 可见，我们可以通过修改 __code__ 来改变 fn 的执行方式。

# 在 Python 中，函数也是一个对象，它也可以被赋值给一个变量，所
