import weakref
# Test weakref.ref(B())

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

class C:
    def __del__(self):
        print("del")

a = A(10)
w1 = weakref.ref(C())
w2 = weakref.ref(a)
print(a)
w1().foo
print(w2)
del w1, w2, w3, w4, w5, w6
import gc
gc.collect()
