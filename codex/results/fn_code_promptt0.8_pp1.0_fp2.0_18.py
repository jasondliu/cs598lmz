fn = lambda: None
# Test fn.__code__.co_argcount

def f1():
    pass

fn.f1 = f1
print(fn.f1.__code__.co_argcount) # 0

def f2(x):
    pass

fn.f2 = f2
print(fn.f2.__code__.co_argcount) # 1

def f3(x, y):
    pass

fn.f3 = f3
print(fn.f3.__code__.co_argcount) # 2

# Example of using co_argcount
for i in range(1, fn.f3.__code__.co_argcount + 1):
    print(i) # prints out 1, 2

# Method 1: __init__

class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

p = Person('Alice')
print(p.get_name()) # prints out 'Alice'

# Method 2: __new__

class Person2:
   
