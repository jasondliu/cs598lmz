import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
weakref.ref(a.c,callback)
del a
del a.c
del keepali0e
gc.collect()
lst[0]

class A(object):
    def __init__(self):
        self.a=1
        self.b=2
        self.c=3
        self.d=4
        self.e=5
        self.f=6
        self.g=7
        self.h=8
        self.i=9
        self.j=10
        self.k=11
        self.l=12
        self.m=13
        self.n=14
        self.o=15
        self.p=16
        self.q=17
        self.r=18
        self.s=19
        self.t=20
        self.u=21
        self.v=22
        self.w=23
        self.x=24

