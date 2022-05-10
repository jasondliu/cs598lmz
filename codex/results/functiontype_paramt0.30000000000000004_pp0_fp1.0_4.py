from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'foo', f.func_defaults, f.func_closure))

# 为了使用它，你需要使用inspect 模块中的getsource() 函数。比如：
from inspect import getsource
getsource(f)

# 如果你只想获取函数的源码的一部分， getblock() 函数会同样有用。比如：
from inspect import getblock
getblock(f)

# 获取函数签名
from inspect import signature
sig = signature(f)
sig

# 这个签名对象有parameters 属性，它是一个有序字典（Order
