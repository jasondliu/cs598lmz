fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# TypeError: 'generator' object is not callable

# 注意，这样是不行的，因为fn.__code__是一个generator,而不是一个function
# 同时，__code__属性也是只读的，所以不能这样写
# fn.__code__ = fn
# fn.__code__()

# AttributeError: 'function' object has no attribute '__code__'

# 这个属性还有一个有用的方法，可以把函数转化为字节码对象
# 下面的例子演示了如何把字节码对象转
