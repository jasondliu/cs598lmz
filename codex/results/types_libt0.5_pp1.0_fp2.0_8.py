import types
types.ClassType

# 创建类
class Person:
    pass

# 创建类的实例
p = Person()

# 给实例添加属性
p.name = 'Mike'
p.age = 25

# 获取实例的属性
print(p.name)
print(p.age)

# 删除实例的属性
del p.age

# 判断实例是否有某个属性
hasattr(p, 'age')

# 获取实例的属性
getattr(p, 'age')

# 设置实例的属性
setattr(p, 'age', 25)

# 删除实例的属性
del
