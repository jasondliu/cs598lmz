import weakref
# Test weakref.ref() without __hash__

class C:
    pass

c = C()
wr = weakref.ref(c)
print(wr)

# Test weakref.ref() with __hash__

class C2:
    def __hash__(self):
        return 42

c2 = C2()
wr2 = weakref.ref(c2)
print(wr2)

# Test weakref.ref() with __eq__

class C3:
    def __hash__(self):
        return 42
    def __eq__(self, other):
        return True

c3 = C3()
wr3 = weakref.ref(c3)
print(wr3)
