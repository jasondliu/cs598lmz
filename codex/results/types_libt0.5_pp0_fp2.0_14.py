import types
types.MethodType(func, obj)

# 给实例绑定属性
obj.name = 'aaa'

# 给实例绑定方法
def func(self):
    print('hello')
obj.func = types.MethodType(func, obj)
obj.func()

# 给类绑定方法
def func(self):
    print('hello')
Student.func = func
Student.func(obj)

# 给类绑定属性
Student.name = '123'
print(Student.name)

# 关于__slots__
'''
如果我们想要限制类实例的属性怎么办？比如，只允许对Student实例添加name和age属
