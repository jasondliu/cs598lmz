import weakref

class Dummy(object):
    def __init__(self, x):
        self.x = x

class WeakRefDict(object):
    def __init__(self):
        self.d = weakref.WeakValueDictionary()

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        return self.d[key]

    def __delitem__(self, key):
        del self.d[key]

    def __len__(self):
        return len(self.d)

    def __contains__(self, key):
        return key in self.d

def test_weakref_dict():
    d = WeakRefDict()
    a = Dummy(1)
    b = Dummy(2)
    d[a] = 3
    d[b] = 4
    assert len(d) == 2
    assert d[a] == 3
    del a
    assert len(d) == 1
    assert b in d
   
