import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print(s.x, s.y, s.z)

# 1 2 3

# 파이썬에서는 이런 구조체를 직접 만들어서 사용할 수 있다.
# 구조체를 만들기 위해서는 ctypes 모듈의 Structure 클래스를 상속받아서 사용한다.
# 구조체의 멤버는 ctypes
