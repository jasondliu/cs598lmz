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

# 파이썬 자료형을 자동으로 변환해준다.

print(s.x + s.y + s.z)

# 배열을 만들 수 있다.

array = (S * 10)()

for i in range(10):
    array[i].x = i
    array[i].y = i * 2
    array[i].z = i * 3

for i in range(10):
    print(array[i].x, array[i].y, array[i].z)

# 함수를 만
