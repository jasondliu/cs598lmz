import ctypes
ctypes = ctypes.cdll.LoadLibrary('./libctypes.so')

ctypes.set_value(1)
ctypes.add_value(10)
print('add_value: ' + str(ctypes.get_value()))

ctypes.sub_value(10)
print('sub_value: ' + str(ctypes.get_value()))
