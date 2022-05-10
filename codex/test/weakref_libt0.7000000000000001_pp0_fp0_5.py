import weakref

def delete(self):
    return self._weakref() is None

class A(object):
    def __init__(self, name):
        self.name = name
        self._weakref = weakref.ref(self, delete)

a = A("A")
