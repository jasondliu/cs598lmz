from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in [f1, f2, f3])
# [<function f1 at 0x10a7d4d08>,
#  <function f2 at 0x10a7d4e18>,
#  <function f3 at 0x10a7d4ea0>]

# 可以看到，这里的函数f1，f2，f3是完全相同的。
# 但是这种做法太过麻烦，我们可以使用copy_func函数来复制一个函数：
from types import FunctionType

def copy_func(f, name=None):
    return FunctionType(f.__code__, f.
