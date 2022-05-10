fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# 可以看到TypeError: 'generator' object is not callable，
# 这是因为code对象不能直接调用，它只是一个数据结构，它描述了一个函数的行为，
# 而不是函数本身。

# 下面我们来看看exec函数

# exec函数可以用来执行字符串，字符串中的Python代码将被解释执行。
# 它的三个参数分别是代码字符串、全局变量字典和
