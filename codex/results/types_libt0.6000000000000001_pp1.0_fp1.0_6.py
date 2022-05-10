import types
types.MethodType(my_func, 123)

# привязка объекта к функции с помощью специального метода __set__
class my_descriptor:
    def __init__(self, func):
        self.func = func
        
    def __get__(self, obj, obj_type=None):
        return types.MethodType(self.func, obj)
    
class my_class:
    @my_descriptor
    def my_func(self):
        print(self)
        
obj = my_class()
obj.my_func()

# декораторы
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        res = func(*args, **kwargs)
        print("after")
        return res
    return wrapper

