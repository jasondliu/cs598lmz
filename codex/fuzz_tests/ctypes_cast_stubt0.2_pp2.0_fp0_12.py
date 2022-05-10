import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE: https://stackoverflow.com/questions/1712227/is-there-a-way-to-list-all-the-methods-in-an-object
def get_all_methods(cls):
    return [func for func in dir(cls) if callable(getattr(cls, func)) and not func.startswith("__")]

# SOURCE: https://stackoverflow.com/questions/1712227/is-there-a-way-to-list-all-the-methods-in-an-object
def get_all_attributes(cls):
    return [func for func in dir(cls) if not callable(getattr(cls, func)) and not func.startswith("__")]

# SOURCE: https://stackoverflow.com/questions/1712227/is-there-a-way-to-list-all-the-methods-in-an-object
def get_all_properties(cls):
    return
