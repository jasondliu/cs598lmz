from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: None, lambda x: None, lambda x, y=42: None))
# [<function <lambda> at 0x...>, <function <lambda> at 0x...>, <function <lambda> at 0x...>]

# 可以通过设置__closure__或__annotations__来添加额外的信息
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)
plus_3.__closure__
# (<cell at 0x...: int object at 0x...>,)
plus_3.__closure__[0].cell_contents
# 3

# 可以通过设置__annotations__来添加函数参数
