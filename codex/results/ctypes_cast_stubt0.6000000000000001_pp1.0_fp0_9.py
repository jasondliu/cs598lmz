import ctypes
ctypes.cast(c.contents.value, ctypes.py_object).value

# todo:
# https://github.com/seveas/python-ctypeslib/blob/master/ctypeslib/contrib/vk_helper.py

# todo:
# https://stackoverflow.com/questions/35791648/how-to-handle-a-c-struct-pointer-returned-by-a-c-library-in-python
# https://stackoverflow.com/questions/27450149/how-to-convert-c-pointer-to-python-list-or-array
# https://stackoverflow.com/questions/15699296/convert-c-struct-to-python-tuple
# https://stackoverflow.com/questions/29997232/python-ctypes-pointer-to-array-of-structs
