from types import FunctionType
a = (x for x in [1])
print(a)
a = 1
print(type(a))
print(type(int))
print(type(a)==type(int))
print(type(a)==int)
print(isinstance(a,int))
print(isinstance(int,type))
print(type(type)==type)
a = [1,2,3]
b = a[:]
print(b)
b.append(4)
print(b)
print(a)
a = [[1, 2], [2, 3], [4, 5]]
result = [i for i in a if i[1] > 2]
print(result)

result = {i[1] for i in a}
print(result)

result = {i:j for i,j in enumerate(a)}
print(result)

result = {i:j[1] for i,j in enumerate(a)}
print(result)


#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import json
str_json = '{"key
