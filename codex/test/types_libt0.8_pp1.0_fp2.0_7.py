import types
types.MethodType(meth, obj)

# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass

# 然后，尝试给实例绑定一个属性：
s = Student()
