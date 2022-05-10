from types import FunctionType
a = (x for x in [1])
print(a, type(a), type(a) == GeneratorType)

a = lambda x: x
print(a, type(a), type(a) is FunctionType)

a = 3 if 3 else 4
print(a)

a = (x for x in [1])
print(a.gi_frame.f_code)  # 返回生成器函数相关信息，<code object <genexpr> at 0x7f73a1c0a8e0, file "code_type.py", line 7>

# 在 python2.7 中
# <generator object <genexpr> at 0x7f75a46c8d60> <type 'generator'> True
# <function <lambda> at 0x7f75a46f07b8> <type 'function'> True
# 3
# <code object <genexpr> at 0x7f75a46c8b10, file "code_type.py", line 7>
