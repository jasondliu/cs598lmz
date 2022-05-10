import ctypes
ctypes.cast(0, ctypes.c_void_p)
# ctypes.cast(obj, ctypes.py_object)

# ---
# ctypes 객체를 Python객체로 변환할때는 PyObject_AsReadBuffer을 사용한다.
# - 변환된 Python 객체의 타입은 bytes 또는 bytearray 타입이다.

# ctypes의 메모리 구조를 Python에서 접근하기
# - 먼저 메모리 배열을 선언하여 그 주소를 반환하고,
# - Python 배
