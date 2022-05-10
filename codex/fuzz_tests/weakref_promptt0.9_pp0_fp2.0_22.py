import weakref
# Test weakref.ref()
import gc

class A:
    def __init__(self):
        self.x = 1

a = A()
a_ref = weakref.ref(a)
a_id = id(a)

a2 = A()
a2_ref = weakref.ref(a2)
a2_id = id(a2)

print([a_ref], a_id)
print([a2_ref], a2_id)

del a

print([a_ref], a_id)
print([a2_ref], a2_id)

a=a_ref()
print(a)

del a
try:
    a2=a2_ref()
except ReferenceError as error:
    print(error)

class A(object):
    def __init__(self):
        self.__a = 1

    def a(self):
        return self.__a

a = A()
a_ref = weakref.ref(a)
a_id = id(a)

del a

try:
