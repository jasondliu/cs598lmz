from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(a.gi_code)
print(a.gi_frame)
print("=====================================================================")
b = FunctionType(a.gi_code, globals(), None, None, a.gi_frame)
print(b)
print(type(b))
print("=====================================================================")
try:
    # 报错，因为 Generator 对象不支持call调用
    b()
except TypeError as e:
    print(e)


def mygenerator(x):
    # 此处的yield是重点，yield后面必须是生成器函数，否则生成器函数会被直接执行
    yield (y for y in range(x))


print("=====================================================================")
mygen =
