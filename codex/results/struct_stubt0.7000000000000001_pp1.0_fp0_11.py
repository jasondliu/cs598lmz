from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda : 1
#print hex(id(s))
#print hex(id(s.size))
#print hex(id(s.size()))
print hex(id(s.size).__hash__())
print hex(id(s.size()).__hash__())
print hex(id(s).__hash__())

print "------------------------------------------------------"

class C(object):
    pass

c = C()
c.attr = 'spam'
print c.__dict__
print c.__class__
print C.__dict__

print "------------------------------------------------------"

class D(object):
    def __init__(self):
        self.attr = 'spam'

d = D()
print d.__dict__
print d.__class__
print D.__dict__

print "------------------------------------------------------"

class E(D):
    pass

e = E()
print e.__dict__
print e.__class__
print E.__dict__

print "------------------------------------------------------"

class F(object
