from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda').__code__.co_freevars)

# [<cell at 0x7f9b5f2b5d08: str object at 0x7f9b5f2b5e88>]

# 使用cell对象来访问闭包中的变量
def make_adder(augend):
    def add(addend):
        return augend + addend
    return add

add_5 = make_adder(5)
add_5.__closure__[0].cell_contents

# 5

# 创建一个类似于列表的对象，但是只存储最后的N个元素
from collections import deque
class LastN(object):
    def __init__(self, n):
        self.n = n
        self.deque = deque()

    def append(self, value):
        if
