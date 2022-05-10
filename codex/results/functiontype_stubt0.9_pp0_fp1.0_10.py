from types import FunctionType
a = (x for x in [1])
# print((lambda x:x)())
class A():
    a=0
    def b(self):
        return self.a
a = A()
print(dir(a))

dir_ = dict()
dir_['a'] = getattr(a,'b')
a.a = 1
map(a.b,[1])
print type(a.a)

a='''
def a(x):
    return x
exec "def a(x):return x*x"
'''
d= {}
e= A()
e.a=a
print a
exec e.a
print a
print locals()

g = (x for x in [1,2,3])
print g
print type(g)
print g.next()
print g.next()
print g.next()
# print g.next()
print [x for x in [1,2,3]]
l = list([1,2,3,4])
l.append(5)
print l
d = {}
d['e']=8
print d
print globals
