from types import FunctionType
list(FunctionType(lambda: None, globals()))

# 从上面的例子可以看出，只有在没有参数的情况下，list()函数才会把字符串 s 当成一个序列，否则它总是当成一个可迭代对象来处理的。
# 所以，为了让 list() 函数按照我们的意愿工作，我们可以传入一个可迭代对象，而不是一个普通的对象。
# 比如，我们可以传入一个列表实例
