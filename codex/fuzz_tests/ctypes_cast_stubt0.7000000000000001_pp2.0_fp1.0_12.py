import ctypes
ctypes.cast(p_float, ctypes.py_object).value

# 파이썬 객체를 직접 사용하여 캐스팅
p_obj = ctypes.cast(p_float, ctypes.py_object)
p_obj.value

# 파이썬 객체에서 원래 객체 참조
p_obj.value = [1, 2, 3]
cast(p_obj, POINTER(c_float))[0]

# 출력 형식을 지정하여 출력
format(cast(p_obj, POINTER(c_float))[0], '.3f')

# 배열 뷰를 사용하여 다차원
