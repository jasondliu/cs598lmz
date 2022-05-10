import types
types.MethodType(func, instance)

# 关于__slots__
# 只对当前类起作用，对子类不起作用
# 只对当前类的实例起作用，对子类的实例不起作用

# 关于@property
# 把一个方法变成属性调用
# 只读属性

# 关于__str__和__repr__
# __str__返回用户看到的字符串
# __repr__返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务
