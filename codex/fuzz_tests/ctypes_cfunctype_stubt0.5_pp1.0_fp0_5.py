import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
fun()

# class
class MyClass(object):
    def __init__(self, name):
        self.name = name

    def my_method(self):
        return self.name

obj = MyClass("my object")
obj.my_method()

# function
def my_function(name):
    return name

my_function("my function")

# lambda
my_lambda = lambda: "my lambda"
my_lambda()

# instance method
class MyClass(object):
    def __init__(self, name):
        self.name = name

    def my_method(self):
        return self.name

obj = MyClass("my object")
obj.my_method()

# class method
class MyClass(object):
    def __init__(self, name):
        self.name = name

    @classmethod
    def my_method(cls):
        return cls.__name__

obj = MyClass("my object")
obj.my_method()

# static method
class My
