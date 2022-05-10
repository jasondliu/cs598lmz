import types
types.MethodType(func, None, None)

# 实例属性和类属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
# 给一个实例绑定的方法，对另一个实例是不起作用的：
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许
