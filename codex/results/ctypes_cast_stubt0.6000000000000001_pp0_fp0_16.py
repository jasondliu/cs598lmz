import ctypes
ctypes.cast(5, ctypes.py_object)
 
# 5

>>> ctypes.cast(5, ctypes.py_object).value

# 5

# ctypes.pythonapi是一个python api接口

>>> ctypes.pythonapi.PyFile_AsFile.restype = ctypes.POINTER(FILE)
>>> ctypes.pythonapi.PyFile_AsFile.argtypes = [ctypes.py_object]
>>> import sys
>>> ctypes.pythonapi.PyFile_AsFile(sys.stdout)

<__main__.LP_FILE object at 0x000001EF5FECE348>

>>> ctypes.pythonapi.PyFile_AsFile(sys.stdout).contents

<__main__.FILE object at 0x000001EF5FECE4C8>

# 使用pythonapi接口获得一个python对象引用

>>> ctypes.pythonapi.Py_InitModule4.restype = ctypes.py_object
>>>
