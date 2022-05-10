from _struct import Struct
s = Struct.__new__(Struct)
s.size = 10
print(s)
print(s.format)
print(Struct.format(s))
print(s.format == Struct.format(s))

# class
print('\n# class')


class Class:

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = Class()
print(obj, obj.method())
print(obj, obj.classmethod())
print(obj, obj.staticmethod())

print(Class, Class.classmethod())
print(Class, Class.staticmethod())


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'


Pizza(['cheese', 'tomatoes'])

Pizza.__repr__(Pizza(['cheese', 'tom
