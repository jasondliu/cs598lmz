import types
types.MethodType

class Student(object):
    pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

s.set_age = types.MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) #调用实例方法
print(s.age) # 测试结果

s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法

def set_score(self, score):
    self.score = score
