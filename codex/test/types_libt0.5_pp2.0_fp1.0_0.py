import types
types.MethodType(f, None, Student)

# 创建实例
s = Student('Michael', 25)
s.name
s.score

# 实例也可以绑定属性
s.name = 'Bob'
s.name

# 给实例绑定方法
def set_age(self, age):
    self.age = age

