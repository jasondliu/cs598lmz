fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

#测试结果：
#PYTHON 3.7 及以上版本报错 TypeError: 'code' object is not iterable
#PYTHON 3.6 及以下版本报错 TypeError: 'generator' object is not callable
