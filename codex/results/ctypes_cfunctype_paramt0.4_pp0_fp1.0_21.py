import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def add(a, b):
    return a + b

add_c = FUNTYPE(add)
print(add_c(1, 2))

def add_c_wrapper(a, b):
    return add_c(a, b)

print(add_c_wrapper(1, 2))

# 파이썬에서 자주 사용하는 함수들의 포인터를 얻어보자.
print(add.__code__.co_code)
print(add.__code__.co_code.hex())

# 포인터를 얻은 후에는 이를 함수로 다시 변환할
