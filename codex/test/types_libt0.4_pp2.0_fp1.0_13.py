import types
types.MethodType(func, obj)

# 如果要给一个实例绑定的方法，可以直接给实例绑定
# 如果要给所有实例绑定方法，可以给class绑定方法

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一
