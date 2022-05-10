import types
types.MethodType(str, None)

# %%
class MyClass:
    def __init__(self):
        self.x = 0

    def increase(self):
        self.x += 1

my_object = MyClass()
my_object.increase()
print(my_object.x)

# %%
class MyClass:
    def __init__(self):
        self.x = 0
        print("x has been set to 0")

    def increase(self):
        self.x += 1
        print("x has been increased")

my_object = MyClass()
my_object.increase()
print(my_object.x)

# %%
class MyClass:
    def __init__(self):
        self.x = 0

    def increase(self):
        self.x += 1

my_object = MyClass()
my_object.increase()

def increase(self):
    self.x += 2

MyClass.increase = types.MethodType(increase, None)
my_object.increase()


