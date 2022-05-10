import weakref

def _t():
    print("called")
    return 10

class A:
    def __init__(self):
        self.b = B(self)

    def t(self):
        return _t()

class B:
    def __init__(self, a):
        self.a = weakref.ref(a)

a = A()
print(a.t())
a = None
print(_t())
