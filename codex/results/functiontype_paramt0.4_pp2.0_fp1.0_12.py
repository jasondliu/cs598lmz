from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# __dict__
class C:
    pass
C.__dict__

# __getattribute__
class C:
    def __getattribute__(self, name):
        return 'foo'
C().__dict__

# __getattr__
class C:
    def __getattr__(self, name):
        return 'foo'
C().__dict__

# __get__
class C:
    def __get__(self, instance, owner):
        return 'foo'
C().__dict__

# __set__
class C:
    def __set__(self, instance, value):
        pass
C().__dict__

# __delete__
class C:
    def __delete__(self, instance):
        pass
C().__dict__

# __setattr__
class C:
    def __setattr__(self, name, value):
        pass
C().__dict__

# __delattr__
class C:
    def __delattr__(self, name):

