import types
types.ClassType

# 创建类
class Person():
    pass

# 类属性与方法
class Person():
    name = 'Person'

    def say_name(self):
        print(self.name)

person = Person()
print(person.name)
print(person.say_name())

# 使用__len__方法定义len函数
class Person():
    name = 'Person'

    def __len__(self):
        return 100

person = Person()
print(len(person))

# 类属性和实例属性
# 类属性 和实例属性对比
class Person():
    name = 'Person'

perso
