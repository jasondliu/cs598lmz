import types
types.MethodType(f,None,Dog)

# __slots__
'''
    使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
'''
class GraduateStudent(Student):
    pass
s = GraduateStudent()
