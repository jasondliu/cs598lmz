from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
a.__next__()

print(type(a)==type(b)==type(c)==FunctionType)
print(type(a)==type(b))
print(type(a)==type(c))
print(type(b)==type(c))

#generator用法
#generator解决一次性处理数据时内存溢出
#generator可以节省内存

import os
def get_pipline():
    with open(r'D:\Desktop\PI_DECIMAL.txt','r') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            yield data
    f.close()
    
g = get_pipline()
t = next(g)
print(t)

#迭代器模式
