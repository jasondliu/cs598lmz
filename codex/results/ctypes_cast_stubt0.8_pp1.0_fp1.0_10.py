import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

obj = None
id(obj)
ctypes.cast(id(obj), ctypes.py_object).value


# 7.6. 其他一些想法

# 7.6.1. 使用 threading 模块中的 local 对象
import threading

local = threading.local()

def process_student():
    std = local.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 通过全
