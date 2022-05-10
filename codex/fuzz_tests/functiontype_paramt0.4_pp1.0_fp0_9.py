from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']

# 我们可以使用inspect模块的signature函数来获取函数的签名
from inspect import signature
sig = signature(tag)
# print(sig)
# (name, *args, cls=None, **kwargs)

# 签名对象的parameters属性是一个有序映射
print(sig.parameters)
# OrderedDict([('name', <Parameter "name">), ('*args', <Parameter "*args">), ('cls', <Parameter "cls=None">), ('**kwargs', <Parameter "**kwargs">)])
