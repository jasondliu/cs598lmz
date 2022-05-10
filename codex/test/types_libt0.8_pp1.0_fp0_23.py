import types
types.MethodType(hello, dog)

dog.eat()

class Dog(Animal):
    __slots__ = ('walk', 'age', 'name')  # 用tuple定义允许绑定的属性名称
    
    def __len__(self):
        return 100
dog = Dog()
len(dog)

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
g.__len__()

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b
    
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
