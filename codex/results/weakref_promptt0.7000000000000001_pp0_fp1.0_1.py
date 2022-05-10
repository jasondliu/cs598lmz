import weakref
# Test weakref.ref

class B(object):
    def __init__(self, arg):
        self.arg = arg
    def method(self):
        return self.arg

class A(object):
    def __init__(self, i):
        self.i = i
        self.refs = [weakref.ref(self) for j in range(10)]
        self.objs = [B(self) for j in range(10)]
        self.weakobjs = [weakref.ref(x) for x in self.objs]

    def method(self):
        return self.i

def test_ref():
    a = A(5)
    assert a.method() == 5
    print a.refs
    for ref in a.refs:
        a1 = ref()
        assert a1 is a
        assert a1.method() == 5
    for obj in a.objs:
        assert obj.method() is a
    for weakobj in a.weakobjs:
        obj = weakobj()
        assert obj.method() is a
   
