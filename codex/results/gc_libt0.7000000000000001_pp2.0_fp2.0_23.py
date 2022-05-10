import gc, weakref

def get_ref_count(address):
    return ctypes.c_long.from_address(address).value

def ref_count(address):
    return get_ref_count(id(address))

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object exists"
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

a = A()

# B has a reference to A
print(ref_count(a))

# Since A has a reference to B,
