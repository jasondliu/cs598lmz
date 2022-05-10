import ctypes
ctypes.cast(0, ctypes.py_object)

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

t = Test(1, 2)
print(t.a, t.b)

t.a = 3
print(t.a, t.b)

del t.b
print(t.a, t.b)

# t.b = 5
# print(t.a, t.b)

print(t.__dict__)


class Test2:
    def __init__(self):
        self.__a = 1

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a

    a = property(get_a, set_a)

t2 = Test2()
print(t2.a)
t2.a = 2
print(t2.a)

class Test3:
    def __init__(self):
        self.__a = 1

   
