import types
types.MethodType(f, None, Student)

# 给实例绑定一个方法
s.print_score = MethodType(f, s)
s.print_score()

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student('Bob', 99)
# s2.print_score()

# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特
