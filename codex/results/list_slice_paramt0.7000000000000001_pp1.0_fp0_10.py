import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)

def test():
    def call_me():
        print('calling me')
    return call_me
f=test()
f()

def test():
    def call_me(x):
        print('calling me with %s'%x)
    return call_me
f=test()
f('ss')

def test():
    def call_me(x,y):
        print('calling me with %s and %s'%(x,y))
    return call_me
f=test()
f('ss','tt')

def test(x,y):
    def call_me(z):
        print('calling me with %s,%s and %s'%(x,y,z))
    return call_me
f=test('ss','tt')
f('z')

def test(x,y):
    def call_me(z,u):
        print('calling me with %s,%s and %s,%s'%(x,y,z,u))
    return call_
