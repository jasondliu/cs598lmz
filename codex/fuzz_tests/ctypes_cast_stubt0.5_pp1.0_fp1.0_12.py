import ctypes
ctypes.cast(0, ctypes.py_object).value

# 字符串编码
# 标准的编码方式是Unicode编码，也叫UTF-8编码。
'ABC'.encode('ascii')
'中文'.encode('utf-8')
'中文'.encode('ascii')
'ABC'.encode('ascii')
'中文'.encode('utf-8')

# 如果把bytes变为str，就必须要指定编码。
b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# len()函数计算的是str的字符数，如果换成bytes
