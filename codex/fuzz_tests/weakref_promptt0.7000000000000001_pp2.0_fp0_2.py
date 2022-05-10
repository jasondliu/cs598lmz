import weakref
# Test weakref.ref(obj) when obj is a class instance
def get():
    return weakref.ref(C())

class C:
    pass

r = get()
print(r().__class__)

# Test weakref.ref(obj) when obj is a class
def get():
    return weakref.ref(object)

r = get()
print(r().__name__)

# Test weakref.ref(obj) when obj is a builtin
def get():
    return weakref.ref(int)

r = get()
print(r().__name__)
# Test weakref.ref(obj) when obj is a function
def get():
    return weakref.ref(f)

def f():
    pass

r = get()
print(r().__name__)
# Test weakref.ref(obj) when obj is a method
def get():
    return weakref.ref(C.f)

class C:
    def f(self):
        pass

r = get()
print(r().__name__)
