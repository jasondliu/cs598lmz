import types
types.MethodType(my_method, p)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('%s は %s 歳です' % (self.name, self.age))


class Test:
    # sample method
    def sample(self):
        print('Class Test sample method')

def my_method():
    print('Class Test my_method')


t = Test()
t.sample()
# t.my_method() # NG
t.my_method = types.MethodType(my_method, t) # t.my_method = my_method でもOK
t.my_method()


p = Person('太郎', 20)
p.greeting()

def my_greeting(self):
    print('%s は %s 歳です' % (self.name, self.age))

# print(p.greeting)
# print(id(p))
#
