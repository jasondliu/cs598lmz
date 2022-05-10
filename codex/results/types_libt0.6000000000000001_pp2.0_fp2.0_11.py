import types
types.MethodType(func, obj)

# 这种动态创建的函数我们称之为绑定方法，它只属于某个实例，而不是整个类。
# 如果想要把一个方法绑到类上，可以使用types.MethodType()将方法绑定到类上，
# 但是绑定到类上的方法只对当前类实例起作用，对其他实例无效。
#
# 练习
# 尝试自己动手定义一个Student类，然后定
