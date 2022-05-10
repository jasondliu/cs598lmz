from types import FunctionType
list(FunctionType(lambda x, y: x + y, globals(), 'add')(1, 2))

# 使用lambda函数
list(map(lambda x: x + 1, [1, 2, 3]))
list(filter(lambda x: x > 2, [1, 2, 3]))
list(reduce(lambda x, y: x + y, [1, 2, 3]))

# 使用functools.partial函数
from functools import partial
list(map(partial(lambda x, y: x + y, 1), [1, 2, 3]))
list(filter(partial(lambda x, y: x > y, 2), [1, 2, 3]))
list(reduce(partial(lambda x, y: x + y, 1), [1, 2, 3]))

# 使用functools.partialmethod函数
from functools import partialmethod
class A:
    def __init__(self, x):
        self.x = x
    def __call__(self, y):
