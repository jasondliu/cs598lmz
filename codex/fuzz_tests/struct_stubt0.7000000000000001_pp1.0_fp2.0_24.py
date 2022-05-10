from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'abc'
s.size = s.calcsize()
s.unpack(b'abc')
# ('a', 'b', 'c')
```

```python
bin(23)
# 0b10111
bin(23)[2:]
# '10111'
```

```python
import calendar
calendar.month(2019, 1)
'''
    January 2019
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
'''
```

```python
d = {'a': 1, 'b': 2}
sorted(d.items(), key=lambda x: x[1])
# [('a', 1), ('b', 2)]
```

## 设计模式

### 原型模式

需要创建重复
