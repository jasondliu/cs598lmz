from types import FunctionType
a = (x for x in [1])
type(a)

print(type(abs), type(a), sep='\n')

# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型
# issubclass()

class Animal(object):
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Husky(Dog):
    pass

husky = Husky()
print(isinstance(husky, Husky))
print(isinstance(husky, Dog))
print(isinstance(husky, Cat))
print(isinstance(husky, Animal))

print(isinstance(husky, int))

# dir()获得一个对象的所有属性和方法
print(dir(husky))

print("属性表
