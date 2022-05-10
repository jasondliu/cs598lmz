from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print type(a)

print type(a.next)
print type(b.next)

print a.next is b.next
print a.next
print b.next

print a.next is a.next
print a.next
print a.next

print FunctionType is type(a.next)

class Test():
    def __init__(self):
        print "Test init"
        self.next = lambda : None
t = Test()
print t.next
print t.next is t.next

x = {'a': 'aaa', 'b': 'bbb'}

print x.viewkeys()
print x.viewvalues()
print x.viewitems()

print x.keys()
print x.values()
print x.items()

y = x.viewkeys()
y.add('c')
print x
print y
