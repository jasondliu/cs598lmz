import ctypes
ctypes.cast(0, ctypes.py_object).value

#https://stackoverflow.com/questions/27858039/c-python-ctypes-how-to-set-a-pointer-to-null-or-none
ctypes.cast(0, ctypes.py_object).value = None

#Test it
a = (1,2)
for i in range(3):
  a, a[i] = a[i:] + a[:i], a
  print(a)
