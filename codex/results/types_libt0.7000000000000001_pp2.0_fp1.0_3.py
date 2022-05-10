import types
types.__dict__

object.__dict__

import math
math.__dict__
```

## 사용자 정의 함수 모듈 만들기
```python
# mod1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

pi = 3.141592
```

```python
import mod1

print(mod1.add(3, 4))
print(mod1.sub(4, 2))
print(mod1.pi)

from mod1 import add
print(add(3, 4))

from mod1 import *
print(add(3, 4))
print(sub(4, 2))
print(pi)
```

## 내장 함수
### 사용자 정의 내장 함수
```python
def mysum(L):
