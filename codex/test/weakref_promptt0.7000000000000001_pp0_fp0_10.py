import weakref
# Test weakref.ref()
# Test weakref.ProxyType()
# Test weakref.ReferenceType()
# Test weakref.getweakrefcount()
# Test weakref.getweakrefs()
# Test weakref.ProxyType.__new__()
# Test weakref.ReferenceType.__new__()
# Test weakref.ProxyType.__init__()
# Test weakref.ReferenceType.__init__()


class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Foo %r>' % (self.name,)


class FooRef(weakref.ReferenceType):
    def __init__(self, ob):
        self.__dict__.update(weakref.ReferenceType.__init__(self, ob))
        self.name = ob.name


def test_ReferenceType():
    f = Foo('f')
    fr = FooRef(f)
    assert fr.name == 'f'
    print(repr(fr))
