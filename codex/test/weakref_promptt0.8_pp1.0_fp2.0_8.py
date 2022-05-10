import weakref
# Test weakref.ref
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)
a = Point(23, 42)
r = weakref.ref(a)
print(r)
print(r())
print(a)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point(%d, %d)' % (self.x, self.y)
a = Point(23, 42)
r = weakref.ref(a)
del a # The object may be deleted at this point
print(r()) # prints None
print(r() is None)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
