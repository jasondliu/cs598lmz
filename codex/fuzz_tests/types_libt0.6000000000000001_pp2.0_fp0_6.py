import types
types.MethodType

# 实例属性和类属性

# 实例属性
# 可以直接在实例上绑定属性，这种属性是实例属性，对于同一个类的所有实例来说，它们是不同的，互不影响
class Student(object):
    pass

s = Student()
s.name = "Michael"
print(s.name)

# 同一个类的不同实例拥有各自不同的实例属性，互不影响
s2 = Student()
s2.name = "Bob"
print(s2.name
