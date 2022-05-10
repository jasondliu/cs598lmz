import weakref
# Test weakref.ref(Class)
print('weakref.ref(Class)')
class C:
    def __init__(self, name):
        self.name = name
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __del__(self):
        print('C.__del__')

c = C('C name')
wr = weakref.ref(c)
print(wr.getName())
wr().setName('weakref C name')
print(wr().getName())
c = None
print(wr().getName())
wr = None

print()
# Test weakref.ref(int)
print('weakref.ref(int)')
wr = weakref.ref(1)
print(wr())
