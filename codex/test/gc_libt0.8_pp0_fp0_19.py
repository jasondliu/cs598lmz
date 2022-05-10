import gc, weakref

def test():
    a = get_a()
    assert not a.get_list()
    a.append_list(A())
    assert len(a.get_list()) == 1
    del a
    gc.collect()
    return True

class A (object):
    def __init__(self):
        self.ref = get_a()
    def __del__(self):
        self.ref.remove_list(self)

class A_Ref (object):
    def __init__(self):
        self.list = []
    def append_list(self, obj):
        self.list.append(weakref.ref(obj))
    def get_list(self):
        return [item() for item in self.list]
    def remove_list(self, item):
        for it in self.list:
            if it() is item:
                self.list.remove(it)

a_ref = A_Ref()
def get_a():
    return a_ref
