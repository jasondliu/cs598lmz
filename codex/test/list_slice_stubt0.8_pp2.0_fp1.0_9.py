import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(len(lst))
weakref.ref(a,callback)
lst.append(str())
del lst[0]

print(lst[0] is None)

class Test(object):

    def __init__(self,name):
        self.name=name

def test(x):print('del %s'%x.name)
a=Test('a')
b=Test('b')
print(a.name,b.name)
weakref.ref(a,test)
weakref.ref(b,test)
keepalive=[]
print(lst[0] is None)
lst=[str()]
a.c=b
print(lst[0] is None)
print(a.name,b.name)
del a
del b
print(lst)
def test1(x):
    print('del %s'%x.name)
lst=[str()]
a=Test('a')
a.name='a1'
b=Test('b')
