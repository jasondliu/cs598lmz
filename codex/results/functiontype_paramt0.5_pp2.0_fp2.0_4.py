from types import FunctionType
list(FunctionType(f.__code__, f.__globals__))

# [1, 2, 3]

# 可以看到，第一个参数是f.__code__，实际上是f.__code__.co_code，
# 即函数指令码，而第二个参数是f.__globals__，函数的全局变量。
# 这两个参数的意义已经在前面介绍过了，
# 因此这里就不再赘述。

# 下面我们再看看FunctionType的__new__方法的定义：

FunctionType.__new__.__code__.co_code
# b
