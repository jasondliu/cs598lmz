from types import FunctionType
a = (x for x in [1])
print isinstance(a, FunctionType)
#isinstance会检查一个对象是否是另一个类型的实例，或者是另一个类型的子类的实例。
#这里的isinstance(a, FunctionType)，表示对象a是否是类型FunctionType的实例，如果是，返回True，否则返回False。
#在这个例子中，a是类型generator的实例，而类型generator不是类型FunctionType的子类，所以将返回False。

#type和isinstance
#type是用于获取一
