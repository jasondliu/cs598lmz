import ctypes
ctypes.cast(a, ctypes.py_object).value = 5 # Убрали привязку к A
print(a, id(a))

a = 3
print(a, id(a))

a = "a"
print(a, id(a))

a = {"a": "A"}
print(a, id(a))

a = [1,2,3]
print(a, id(a))

def f():
    pass

a = f
print(a, id(a))
