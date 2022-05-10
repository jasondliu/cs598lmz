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
print ref(), '\n', ref(), '\n', ref() is None and 'None' or ref()
del a
print ref(), '\n', ref(), '\n', ref(), '\n', ref() is None and 'None' or ref()
# Test weakref.proxy supports cyclic references.
class TestProxy:
    def __init__(self, name):
        self.name=name
    def __str__(self):
        return self.name
def testproxy():
    a=TestProxy('a')
    b=TestProxy('b')
    a.x=b
    b.x=a
    ref=weakref.proxy(a)
    print ref, '\n', ref.x, '\n',
