import gc, weakref
class C(object):
    def __del__(self):
        print self, 'deleted'
c = C()
print c, c.__del__
print weakref.ref(c)
c = None
print gc.collect()

# reference chain
class A:
    def __del__(self):
        print "class A is deleted"
class C:
    def __del__(self):
        print "class C is deleted"
d = A()
e = d
f = e
del d
del e
del f
# gc.collect()

# think about what happed if class C is deri
