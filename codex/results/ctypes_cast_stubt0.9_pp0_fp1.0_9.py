import ctypes
ctypes.cast(id(float), ctypes.py_object).value

"""
The solution uses ctypes to convert the memory address of any Python object into a corresponding
pointer to a Python object. The pointer can then be unwrapped using the Value attribute to get the
object. The ctypes library is a fairly advanced topic and is covered in Recipe 5.8.
"""
