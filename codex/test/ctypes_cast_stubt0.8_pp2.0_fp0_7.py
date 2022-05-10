import ctypes
ctypes.cast(0, ctypes.py_object)

type(None)

class foo():
    pass

foo_instance = foo()

type(foo_instance)

foo.__name__

class foo():
    pass

foo_instance = foo()

class_of_foo_instance = type(foo_instance)

class_of_foo_instance.__name__

class foo():
    pass

foo_instance = foo()

class_of_foo_instance = type(foo_instance)

class_of_foo_instance.__name__ == foo.__name__

class foo():
    pass

foo_instance = foo()

class_of_foo_instance = type(foo_instance)

class_of_foo_instance == type(foo_instance)


class foo():
    x = 2

foo_instance = foo()

class_of_foo_instance = type(foo_instance)

class_of_foo_instance.x == foo.x

class foo():
    x = 2

