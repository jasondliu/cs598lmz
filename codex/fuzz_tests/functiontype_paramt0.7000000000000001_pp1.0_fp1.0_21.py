from types import FunctionType
list(FunctionType(m).__code__.co_consts)

# [None, True, False, 'lo', 'args', 'kwargs', 'return', 'print(args)', 'print(kwargs)']

# 使用__code__属性，我们可以在改变函数的参数列表以及函数体的前提下，对函数进行修改
# 重新组装__code__属性，创建新的函数对象

import dis

def gen_func(params, code):
    """
    :param params: 函数参数列表
    :param code: 函数体
    :return:
    """
    g = {'print': print}
    exec(code, g)
    func = FunctionType(g['func'
