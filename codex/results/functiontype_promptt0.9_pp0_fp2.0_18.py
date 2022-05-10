import types
# Test types.FunctionType
class MyFunctionBase(object):
    def __init__(self, *args, **kwargs):
        super(MyFunctionBase, self).__init__(*args, **kwargs)
        self.definitions = []
    def __call__(self, *args, **kwargs):
        return self
    def __str__(self):
        return "{0}".format(self.__class__)
    def __repr__(self):
        return "{0}".format(self.__class__.__name__)
    def __getattr__(self, name):
        return self
    def __getitem__(self, *args, **kwargs):
        return self
    def __eq__(self, other):
        return self == other
    def __gt__(self, other):
        return self > other
    def __ge__(self, other):
        return self >= other
    def __mul__(self, other):
        return self * other
    def __sub__(self, other):
        return self - other
# class Slice(My
