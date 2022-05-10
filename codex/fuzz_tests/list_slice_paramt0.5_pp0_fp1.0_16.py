import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
lst.append(str())
print(lst)

"""

class A(object):
    def __del__(self):
        print("A.__del__")

def callback(x):
    print("callback")
    del lst[0]

keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)
lst.append(str())
print(lst)
"""
