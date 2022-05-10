from types import FunctionType
a = (x for x in [1]) #生成器
b = [x for x in [1]]
c = list(map(lambda x:1, [1]))
print(type(a))
print(type(b))
print(type(c))
def gen():
    yield 1
print(type(gen()))
print(type(gen))
print(isinstance(gen, FunctionType))
print(isinstance(gen(), generator))
```

```
#列表解析修改
print([i+30 if i > 20 else i+20 if i > 10 else i+10 for i in range(1, 51)])
```

```
#lamda表达式修改
original_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x + 10 if x > 5 else x + 0 if x > 3 else x + 1, original_num)))
```

```
try:
    pass
except:

