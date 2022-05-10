import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.proxy(a,callback))
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.proxy(lst,callback))
keepali0e.append(weakref.ref(lst,callback))
print(keepali0e)
'''
a=A()
a.c=a
lst=[str()]

keepalive=[weakref.proxy(a),weakref.ref(a),weakref.proxy(lst),weakref.ref(lst)]

print(keepalive)
