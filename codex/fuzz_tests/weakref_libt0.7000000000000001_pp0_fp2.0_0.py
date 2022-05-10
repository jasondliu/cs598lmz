import weakref
import gc


class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Weaker:
    def __init__(self):
        self.a = A(10)
        self.wref = weakref.ref(self.a)

    def callback(self, x):
        print(x)

    def __del__(self):
        print("Deleted")


w = Weaker()
print(w.a)
print(w.wref)
print(w.wref())
print(w.wref() is w.a)
print(w.wref() == w.a)
print(w.wref() is None)
w = None
gc.collect()
print("-----------------------")


class Person:
    def __init__(self, name, surnamr, address):
        self.name = name
        self.surname = surnamr
        self.address = address

    def __repr__(
