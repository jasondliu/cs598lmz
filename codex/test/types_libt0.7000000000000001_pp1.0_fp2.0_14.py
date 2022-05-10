import types
types.MethodType(randpass, admin)
admin.randpass()

# 使用__slots__
class User(object):
    __slots__ = ('name', 'age')

class GraduateStudent(User):
    pass
