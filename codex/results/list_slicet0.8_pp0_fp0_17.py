import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
''')
        self.check('import weakref')
        if sys.version_info >= (2, 3):
            self.check('import gc')
            self.check('gc.collect()')
            self.check('lst=[]')
        self.check('''
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[""]
a=A()
a.c=a
wr=weakref.ref(a,callback)
keepali0e.append(wr)
del a
while lst:keepali0e.append(lst[:])
''')
        self.check_exception(weakref.ReferenceError, 'wr()')

    def test_weakref_proxy(self):
        self.check('import weakref')
        self.check('import pickle')
        self.check('''
class A(object): pass
a = A()
def f(): pass
wr = weakref.ref(a, f)
pp = wr.proxy()
result = wr()
