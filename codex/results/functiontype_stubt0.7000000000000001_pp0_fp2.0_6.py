from types import FunctionType
a = (x for x in [1])
print(type(a))
# <class 'generator'>
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.__name__, a.gi_closure)
print(type(b))
# <class 'function'>
print(b())
# 1

# B.2.2.3 函数对象的特殊属性
# 函数对象还有几个特殊属性，这些属性大多跟函数本身的调用有关，通常情况下是不需要关注它们的。
def foo():
    a = 1
    b = 2
    return a+b
print(foo.__code__)
# <code object foo at 0x7f6a5c9d9fb0, file "<stdin
