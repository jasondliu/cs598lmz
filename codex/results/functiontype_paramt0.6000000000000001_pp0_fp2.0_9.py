from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), "f")(2))

# todo: (1) 通过高阶函数创建多个函数

# todo: (2) 通过类创建多个方法
class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}
    def __call__(self, *args):
        types = tuple(arg.__class__ for arg in args) # a generator expression!
        function = self.typemap.get(types)
        if function is None:
            raise TypeError("no match")
        return function(*args)
    def register(self, types, function):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = function

# Example use
def vect2(x, y):
    return (x, y)


