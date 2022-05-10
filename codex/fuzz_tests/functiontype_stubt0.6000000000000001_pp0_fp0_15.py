from types import FunctionType
a = (x for x in [1])
print(type(a))
#<class 'generator'>

def test():
    yield 1
    yield 2
    yield 3

print(type(test))
#<class 'function'>
print(type(test()))
#<class 'generator'>

print(isinstance(test, FunctionType))
#True
print(isinstance(test(), GeneratorType))
#True
```

```python
# 判断是否可迭代
from collections import Iterable

print(isinstance([1], Iterable))
#True
print(isinstance({"name": "zhangsan"}, Iterable))
#True
print(isinstance((1,), Iterable))
#True
print(isinstance("123", Iterable))
#True
print(isinstance(123, Iterable))
#False

# 判断是否可迭代且迭代出的元素为字符串
from collections import Iterator
print(isinstance([1], Iterator))

