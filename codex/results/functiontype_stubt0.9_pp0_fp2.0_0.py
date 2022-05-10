from types import FunctionType
a = (x for x in [1])
b = list((x for x in [1]))

print(type(a))
print(type(b))
print(a)
print(b)

print('islice>>>>>>>>>')
import itertools
for i in itertools.islice(itertools.count(),1,5):
    print(i)

#map可以用iter(map())把返回的map对象转化成迭代器
def f(x):
    return x**2
a_map=map(f,[1,2,3])
for i in iter(a_map):
    print(i)

print('zip>>>>>>>>>')
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
print(list(zip(a, b)))  
print(list(zip(*a)))  # 和itertools.izip()取笛卡尔积
print(list(itertools.izip(*a))) 
