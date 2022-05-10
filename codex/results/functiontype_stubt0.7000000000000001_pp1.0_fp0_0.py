from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
print(isinstance(a, object))

# finally 在try语句中无论是否发生异常，都会执行到
try:
    print('Try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 可选的else语句，必须放在所有的except语句之后，如果try中没有发生错误，则执行else语句
try:
    print('Try...')
    r = 10 / 2
    print('result:', r)
