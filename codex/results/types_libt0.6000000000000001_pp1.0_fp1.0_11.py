import types
types.MethodType(method, obj, obj)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eat')

    def drink(self):
        print('drink')

    def sleep(self):
        print('sleep')

    def work(self):
        print('work')


def play(self):
    print('play')


def play_ball(self, what):
    print('play %s' % what)


def get_name(self):
    print(self.name)


def set_name(self, name):
    self.name = name


p = Person('yuan', 18)
print(p.name)
p.eat()
p.drink()
p.sleep()
p.work()

# 动态给对象绑定方法
p.play = types.MethodType(play, p)
p.play()
p.play_ball = types.
