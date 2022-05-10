from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))

# generator 可以被 next() 函数调用，返回下一个值
for i in (x for x in range(10)):
    print(i)

# generator 可以被 for 循环遍历
for i in (x for x in range(10)):
    print(i)

# generator 可以被 yield from 调用
def gen():
    for x in range(10):
        yield from (x for x in range(10))

for i in gen():
    print(i)
