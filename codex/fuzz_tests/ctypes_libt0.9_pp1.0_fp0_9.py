import ctypes
ctypes.c_float(3.3)

# 다양한 숫자형 타입
ctypes.c_byte(1)
ctypes.c_ubyte(1)
ctypes.c_short(1)
ctypes.c_ushort(1)
ctypes.c_int(1)
ctypes.c_uint(1)
ctypes.c_longlong(1)
ctypes.c_ulonglong(1)

# 문자열
ctypes.c_char_p(b'Hello, World')

# void 포인터
ctypes.c_void_p(-1)

```

```python
# 심볼 테이블을 사용하여 함수 목록 출력하기
# 이 방법을 사용하
