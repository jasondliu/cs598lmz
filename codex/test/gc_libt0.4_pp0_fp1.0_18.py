import gc, weakref, sys

def show_all_objects():
    for obj in gc.get_objects():
        print(obj)

def ref_count(address: int):
    return sys.getrefcount(address)

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            print('Found object by id: ', obj)
            break

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
print
