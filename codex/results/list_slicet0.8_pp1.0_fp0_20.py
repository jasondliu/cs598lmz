import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])"""
        self.run(snippet, ["[str(), [[], []]]"])

    def test_simple_callback(self):
        snippet = """
l=[1,2,3]
def callback(x):print 'boe',x
def f():
    l.append(4)
    l.pop(0)
    l.append(5)
    l.pop(0)
    l.append(6)
    l.pop(0)
    l.append(7)
    l.pop(0)
    l.pop(0)
def g():
    l.append(8)
    l.pop(0)
    l.pop(0)
    l.pop(0)
    l.pop(0)
    l.pop(0)
    l.pop(0)
    l.pop(0)
def h():
    l.append(9)
    l.pop(0)
    l.pop(0)
    l.pop(0)
    l.pop(0)
    l.pop(0)
