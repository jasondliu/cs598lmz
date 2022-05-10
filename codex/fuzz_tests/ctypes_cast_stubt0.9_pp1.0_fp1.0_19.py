import ctypes
ctypes.cast(id(1), ctypes.py_object).value

id_int = id(1)

py_obj = ctypes.py_object(1)
print (py_obj)
print (py_obj.value)

print (type(py_obj))
print (type(py_obj.value))

## 強制的にポインタ辞書型に変換
def to_dict(pyobj):
    pobj =  ctypes.cast(id(pyobj), ctypes.POINTER(ctypes.py_object))[0]
    address = id(pyobj)
    print (pobj)
    return pythonapi.PyDict_GetItem(pobj, pyobj)#.value

print(
    to_dict({1:2})
)

# どうもここら辺りの内部実装的な物をPythonのモジュールから私が変えたり直指定して処
