import ctypes
ctypes.cast(id(5), ctypes.py_object).value

# 파이썬은 모든것이 객체다!

# 일반적인 방법
t1 = (1, 2, 3)
t2 = (4, 5)
t1 + t2

# 위의 코드를 보면, t1이나 t2는 변하지 않는다.
# 하지만 아래의 코드는 변한다.
t1 = (1, 2, 3)
id(t1)

t1 += (4, 5)
id(t1)

# 튜플의 경우, 새로운 객체를
