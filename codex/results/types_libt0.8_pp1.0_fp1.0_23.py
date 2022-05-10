import types
types.MethodType(f, None, Person)  # 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
class Student(object):
	__slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
								 # __slot__定
