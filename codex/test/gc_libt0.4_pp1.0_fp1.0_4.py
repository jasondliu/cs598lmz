import gc, weakref

def get_object_by_id(id):
    for obj in gc.get_objects():
        if id(obj) == id:
            return "Object exists"
    return "Not found"

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))

gc.disable()
my_var = A()
a_id = id(my_var)
b_id = id(my_var.b)
