import weakref
# Test weakref.ref().

class Foo:

    def __init__(self, name):
        self.name = name
        self.refs = []

    def AddRef(self, r):
        self.refs.append(r)

    def __del__(self):
        print "Foo.__del__"

def bar(f):
    f.AddRef(weakref.ref(f))

f = Foo("foo")
f.AddRef(weakref.ref(f))
bar(f)
del f

class Foo2:

    def __init__(self, name):
        self.name = name
        self.refs = []

    def AddRef(self, r):
        self.refs.append(r)

    def __del__(self):
        print "Foo2.__del__"
        print self.name, self.refs

def bar2(f):
    f.AddRef(weakref.ref(f))

f = Foo2("foo")
f.AddRef(weakref.ref(f))
bar2
