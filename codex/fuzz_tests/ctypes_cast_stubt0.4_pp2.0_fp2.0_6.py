import ctypes
ctypes.cast(0, ctypes.py_object).value

# 파이썬 프로그램이 가진 모든 객체는 참조 계수를 가지고 있다.
# 참조 계수가 0이 되면 객체는 제거된다.
# 참조 계수가 0이 되면 제거되는 시점은 다음과 같다.
# 1. 파이썬이 실행하는 스크립트가 끝나면
#
