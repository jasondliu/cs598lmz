import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int
)

# -----------------------------------------------------------

# -----------------------------------------------------------
# Define a new class and its methods.

class MyClass(object):
    # This method is a class method.
    @classmethod
    def class_method(cls):
        print("{0}::class_method()".format(cls.__name__))

    # This method is a static method.
    @staticmethod
    def static_method():
        print("MyClass::static_method()")

    # This method is a normal method.
    def normal_method(self):
        print("MyClass::normal_method()")

# -----------------------------------------------------------

# -----------------------------------------------------------
# Define a new exception and its methods.

class MyException(Exception):
    # This method is a class method.
    @classmethod
    def class_method(cls):
        print("{0}::class_method()".format(cls.__name__))

    # This method is
