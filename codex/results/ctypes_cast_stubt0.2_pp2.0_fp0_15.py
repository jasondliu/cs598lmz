import ctypes
ctypes.cast(0, ctypes.py_object).value

# 파이썬의 객체는 실제로 파이썬이 사용하는 메모리 공간의 주소를 가리키는 포인터이다.
# 이런 포인터를 파이썬에서는 참조(reference)라고 부른다.
# 참조는 객체를 가리키는 포인터이므로 객체의 주소를 저장
