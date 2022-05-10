from types import FunctionType
list(FunctionType(
    (
        (lambda: 0),
        'name',
        'doc',
        (0,),
        None
    ),
    {},
    '__defaults__',
    (10,),
    None
).__reduce__())
# [<function __main__.<lambda>()>, (), (0,), None, None]

def f(x):
    def g(y):
        return x * y
    return g

import copy
copy.deepcopy(f(10))(5)
# 50

# __code__
# 可以对函数对象中的co_code等属性进行操作
import dis
def f(x):
    print(x)

dis.dis(f)
#  2           0 LOAD_GLOBAL              0 (print)
#              3 LOAD_FAST                0 (x)
#              6 CALL_FUNCTION            1
#              9 POP_TOP
#             10 LOAD_CONST               0 (
