import types
types.MethodType(func, None, MyClass)
# <unbound method MyClass.fun>

# 2. 给实例绑定一个方法
obj = MyClass()
types.MethodType(func, obj, MyClass)
# <bound method MyClass.func of <__main__.MyClass object at 0x00000000030F2320>>

# 3. 给一个实例绑定的方法，对另一个实例是不起作用的
obj2 = MyClass()
obj2.func
# <bound method MyClass.func of <__main__.MyClass object at 0x00000000030F2390>>

# 4. 使用__slots__
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()
s.name =
