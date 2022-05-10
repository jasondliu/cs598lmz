import types
types.MethodType(func, obj)

# 通过实例变量的__dict__属性来访问
obj.__dict__['x']

# 类的__dict__属性，用来查看类的属性
# dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir('ABC')

# 使用__slots__
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作
