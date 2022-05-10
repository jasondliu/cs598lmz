import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
ref=weakref.ref(a,callback)
del a
gc.collect()
print lst

class A(object):
    def __init__(self,a):
        self.a=a
    def __del__(self):
        print "in del"
    def __eq__(self,o):
        return self.a==o.a
    def __ne__(self,o):
        return self.a!=o.a
    def __lt__(self,o):
        return self.a<o.a
    def __le__(self,o):
        return self.a<=o.a
    def __gt__(self,o):
        return self.a>o.a
    def __ge__(self,o):
        return self.a>=o.a
    def __hash__(self):
        return self.a
    def __hash__(self):
        return self.a
    def __nonzero__(self):
        return self.a
    def __getattr
