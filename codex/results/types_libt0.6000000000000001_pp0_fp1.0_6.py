import types
types.MethodType(f, None, Student)
# 给实例绑定一个方法
s = Student()
s.set_score = types.MethodType(f, s)
s.set_score(100)
s.score

# 给class绑定方法后，所有实例均可调用
s2 = Student()
s2.set_score(99)

# 给class绑定的方法，对其实例是不起作用的
s.set_score(101)

# 使用__slots__
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
