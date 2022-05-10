from types import FunctionType
a = (x for x in [1])
print(a)
try:
    print(a)
finally:
    print('finally')
