import types
types.MethodType(f, None, Student)

# 调用的时候，传入的是实例变量，因此，我们需要把实例变量传进去：
s.set_age(25)  # 调用方法
s.age  # 测试结果

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()  # 创建新的实例
s2.set_age(25)  # 尝试调用方法
# AttributeError: 'Student' object has no attribute 'set_age'

# 为了给所有
