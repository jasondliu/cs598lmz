import weakref
# Test weakref.ref supports cyclic references.
class TestRef:
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return self.name
a=TestRef('a')
b=TestRef('b')
a.x=b
b.x=a
ref=weakref.ref(a)
