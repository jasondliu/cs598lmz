import types
types.MethodType(lambda self: self.get_value() * 2, obj)

# 不能给一个实例绑定一个方法，只能给class绑定
# obj.get_value = lambda self: self.get_value() * 2

# 方法和函数的区别
# 方法是绑定在对象上的，第一个参数是self，self指向对象本身
# 函数没有绑定对象，不需要第一个参数

# 可以通过types.MethodType()动态给一个实例绑定一个方法
# 可以通过types.Function
