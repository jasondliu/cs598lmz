import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(lst[0],callback))
del lst
del keepali0e
a.c=1
a.c=2
a.c=3
a.c=4
a.c=5
""")

if __name__ == '__main__':
    t.main()
