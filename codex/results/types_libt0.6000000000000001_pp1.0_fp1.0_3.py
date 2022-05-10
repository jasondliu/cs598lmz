import types
types.MethodType(method, obj, obj.__class__)

# 动态语言特点
# 对象的属性可以动态的添加和删除
# class Animal(object):
#     pass
#
#
# class Dog(Animal):
#     pass
#
#
# class Cat(Animal):
#     pass
#
#
# dog = Dog()
# cat = Cat()
# print(dog)
# print(cat)
# dog.name = 'haha'
# cat.name = 'lala'
# print(dog.name)
# print(cat.name)

# 实例属性和类属性
# 实例属性只有在实例属性中才可以使用，如果在其他地方使
