from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'foo') for x in range(10))
# [<function foo at 0x7f7c7c0d0e18>, <function foo at 0x7f7c7c0d0ea0>, <function foo at 0x7f7c7c0d0f28>, <function foo at 0x7f7c7c0d0fb0>, <function foo at 0x7f7c7c0d0f28>, <function foo at 0x7f7c7c0d0fb0>, <function foo at 0x7f7c7c0d0f28>, <function foo at 0x7f7c7c0d0fb0>, <function foo at 0x7f7c7c0d0f28>, <function foo at 0x7f7c7c0d0fb0>]

# 使用类来实现
class GenFunc(object):
    def __init__(self, func, name=''):
        self.func = func
        self.name = name
