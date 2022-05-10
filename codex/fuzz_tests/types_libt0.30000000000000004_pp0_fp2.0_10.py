import types
types.MethodType(lambda self: self.value, None, MyClass)
# <unbound method MyClass.__lambda__>

# 关于__slots__
# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__

# 使用@property
# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property
