import weakref
# Test weakref.ref(...).proxy()

class Foo:
    def __init__(self, id):
        self.id = id
        self.refs = []
    def __del__(self):
        print('Foo.__del__(%s)' % self.id)

class Bar:
    def __init__(self, id):
        self.id = id
        self.refs = []
    def __del__(self):
        print('Bar.__del__(%s)' % self.id)

def make_ref(obj, refs):
    refs.append(weakref.ref(obj))

def test():
    f1 = Foo(1)
    f2 = Foo(2)
    b1 = Bar(1)
    b2 = Bar(2)
    make_ref(f1, f1.refs)
    make_ref(f2, f2.refs)
    make_ref(b1, b1.refs)
    make_ref(b2, b2.refs)
    make_ref(
