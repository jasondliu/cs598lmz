import types
types.FunctionType = types.FunctionType
del types

import copy_reg
def reduce_method(m):
    return (getattr, (m.__self__, m.__func__.__name__))
copy_reg.pickle(types.MethodType, reduce_method)
del copy_reg
