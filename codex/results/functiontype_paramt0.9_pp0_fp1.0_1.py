from types import FunctionType
list(FunctionType().__mro__)

# 浅复制和深复制
import copy as c

def type_test(x):
    if isinstance(x, (list,tuple)):
        for i in range(len(x)):
            type_test(x[i])
    elif isinstance(x, dict):
        for m,n in x.items():
            print(m,n)
    print(type(x),x)

a = ['wzw1', ('wzw2',True), {'wzw3':'wzw4', 'wzw5':'wzw6'}]
type_test(a)

type_test(c.copy(a))
type_test(c.deepcopy(a))

# __new__和__init__的区别？__new__是创建对象并返回，__init__是对象类型的初始
