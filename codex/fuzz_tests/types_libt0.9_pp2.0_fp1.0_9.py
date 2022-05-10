import types
types.MethodType(func1,None,p42class)

p42.set_x(10)
print(p42.get_x())


#类的动态绑定
#需要不断加新功能
#继承
class Animal(object):
    def run(self):
        print("animal is running")

class Dog(Animal):
    def run(self):
        print("dog is running")

class Cat(Animal):
    def run(self):
        print("cat is running")

dog=Dog()
dog.run()
cat=Cat()
cat.run()

#检测种类
def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
b = Dog()
run_twice(a)
run_twice(b)

#多态，继承
class Mouse(Animal):
    def run(self):
        print("mouse
