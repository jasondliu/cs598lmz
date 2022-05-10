import ctypes
ctypes.cast(0, ctypes.py_object)

# %%
# 所有的类型都可以转换为ctypes.py_object类型，但是只有ctypes.py_object类型可以转换为其他类型。
# 因此，ctypes.py_object类型可以看成是一个容器，可以装任何类型的数据。
# 可以用ctypes.py_object类型来实现类似于C语言中的void*类型。

# %%
# 在Python中，可以用ctypes.py_object类型来实现
