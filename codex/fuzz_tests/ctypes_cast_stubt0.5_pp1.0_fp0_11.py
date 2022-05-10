import ctypes
ctypes.cast(0, ctypes.py_object).value

# 파이썬 방식
try:
    print(1 / 0)
except ZeroDivisionError:
    print('error')

# ctypes 방식
try:
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(0), ctypes.py_object(ZeroDivisionError))
except ZeroDivisionError:
    print('error')

# 다중 스레드 예외 발생 테스트
import threading
import time

def thread_function():
    time.sleep(1)
    raise ZeroDivisionError

thread = threading.Thread(target=thread_function)
thread.start()

try:
    ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), ctypes.py_object(ZeroDivisionError))
except ZeroDivisionError:
