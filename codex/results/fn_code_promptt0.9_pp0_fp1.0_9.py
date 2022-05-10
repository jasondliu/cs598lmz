fn = lambda: None
# Test fn.__code__
#>>> import dis
#>>> dis.dis(fn)
#>>> dis.dis(fn.__code__)
# NameError: name '__code__' is not defined
class A(object):
    def __init__(self, *args):
        print('__init__')
        self.args = args
    
    def __new__(cls, *args):
        print('__new__')
        self = super().__new__(cls)
        return self
    
    def __getitem__(self, index):
        print('__getitem__')
        return self.args[index]
    
    def __missing__(self, item):
        print('keyerror')
    
    @property
    def abc(self):
        print('property')
        return 2


a = A(4, 5, 6)

# >>> a[:2]
a.abc

a['a']

a[4]

class B:
    def __init__(self, *args):
        print('B.__init__')

