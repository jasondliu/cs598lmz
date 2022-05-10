import types
types.FunctionType

# 查看一个对象的所有属性和方法
dir("ABC")

len("ABC")

"ABC".__len__()

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
len(dog)

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

hasattr(obj, 'x')
obj.x
hasattr(obj, 'y')
setattr(obj, 'y', 19)
hasattr(obj, 'y')
getattr(obj, 'y')
getattr(obj, 'z', 404)

fn = getattr(obj, 'power')
fn()

class Student(object):
    def __init__(self, name):
        self.name = name

s = Student("Bob")
s.score = 90

