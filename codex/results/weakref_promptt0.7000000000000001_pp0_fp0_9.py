import weakref
# Test weakref.ref() with a weakref-able class with a __hash__.

class Foo(object):
    count = 0
    def __init__(self):
        Foo.count += 1
        self.id = Foo.count
        self.hash = hash(self.id)
    def __hash__(self):
        return self.hash

objs = [Foo(), Foo(), Foo(), Foo(), Foo(), Foo(), Foo(), Foo(), Foo()]

class MyDict(dict):
    pass

d = MyDict()
for obj in objs:
    d[weakref.ref(obj)] = 1

for obj in objs:
    if weakref.ref(obj) in d:
        print obj

for obj in objs:
    if weakref.ref(obj) not in d:
        print obj

print "Test complete"
