import weakref
# Test weakref.ref() without __hash__ implementation.
# Does not crash on CPython 3.3 onwards.
class W(weakref.ref):
    def __eq__(self, other):
        return True

x = W(W(W(W(42))))

print(x)
print(dir(x))
print(x())

print(x.__class__)
print(x.__class__.__class__)
print(x.__class__.__class__.__class__)
print(x.__class__.__class__.__class__.__class__)
print(42)

print(W.__class__)
print(W.__class__.__class__)
print(W.__class__.__class__.__class__)

print(x.__bases__)
print(x.__bases__.__bases__)
print(x.__bases__.__bases__.__bases__)
print(x.__bases__.__bases__.__bases__.__bases__)
