import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

## >>> s = S()
## >>> s.x = 10
## >>> s.y = 20
## >>> s.x
## 10
## >>> s.y
## 20
## >>> s.z = 30
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## AttributeError: 'S' object has no attribute 'z'
## >>>

## >>> s = S()
## >>> s.x = 10
## >>> s.y = 20
## >>> s.x
## 10
## >>> s.y
## 20
## >>> s.z = 30
## Traceback (most recent call last):
##   File "<stdin>", line 1, in <module>
## AttributeError: 'S' object has no attribute 'z'
## >>>

## >>> s = S()
## >>> s.x = 10
## >>> s.y = 20
## >>> s.x
## 10
## >>> s.y
## 20
## >>> s.z =
