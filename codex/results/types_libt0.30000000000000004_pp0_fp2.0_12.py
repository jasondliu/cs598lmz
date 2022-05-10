import types
types.MethodType(foo, None, type)
# TypeError: unbound method foo() must be called with type instance as first argument (got nothing instead)

# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 但是，如果Student类本身需要绑定一个属性呢
