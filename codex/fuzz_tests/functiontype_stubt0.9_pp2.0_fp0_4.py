from types import FunctionType
a = (x for x in [1])
b = sum([1, 2, 3])
c = type(int)
print(a)
print(b)
print(c)

# Python中变量的作用域
print('********************')
global_a = 100

def func():
    global_a = 200
    print('global_a:', global_a)
    print(locals())
    global global_a
    print(globals())
    global_a = 300
    print(globals())

func()
print(globals())

# 三种常见的循环对比
# 集合迭代
print('********************')
r = []
for v in [1, 2, 3]:
    r.append(v * v)

print(r)
print([x * x for x in [1, 2, 3]])
print(list(map(lambda x: x * x, [1, 2, 3])))

a = [1, 2, 3, 4
