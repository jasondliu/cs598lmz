import types
types.MethodType(f, None, Student)

### 3.4、实例属性和类属性
'''
9、实例属性和类属性
实例属性就是给实例绑定属性，每个实例的属性都是独立的。
类属性就是给类绑定属性，每个实例可以共享一个类属性。
'''
class Student(object):
    name = 'Student'

g = Student()
g.name        # 实际上形成了一个实例属性 name
g.name='AJ'
print(g.name)
