import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
print(s.x, s.y)

s.x = 50
s.y = 100
print(s.x, s.y)
```

```
0 0
50 100
```

#### 3.2.2 파이썬 타입으로 간접 사용하기

```python
import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
print(s.x, s.y)

s.x = 50
s.y = 100
print(s.x, s.y)
```

```
0 0
50 100
```

### 3.3 포인터

#### 3.3.1 포인
