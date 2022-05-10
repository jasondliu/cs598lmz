fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# 生成器和函数的区别：
# 1.生成器是可迭代对象，函数不是
# 2.生成器可以暂停，函数不行
# 3.生成器每次返回一个值，函数一次性返回所有值
# 4.生成器只能用于循环，函数既可以用于循环，也可以单独调用
# 5.生成器可以接收参数，函数不行
#
