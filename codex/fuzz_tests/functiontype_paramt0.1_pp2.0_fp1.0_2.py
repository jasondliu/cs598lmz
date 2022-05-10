from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# 使用内置的callable()函数，可以判断一个对象是否是“可调用”对象。
callable(abs)
callable(lambda x: x)
callable([1, 2, 3])
callable(None)
callable('str')

# 使用错误处理机制
# 在程序运行的过程中，总会出现各种各样的错误。
# 有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符
